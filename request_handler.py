from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from views import get_all_users, update_user, delete_user
from views import create_post, get_all_posts, update_post, delete_post
from views import get_all_categories, create_category, update_category, delete_category
from views import create_user, login_user



class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def parse_url(self):
        """Parse the url into the resource and id"""
        path_params = self.path.split('/')
        resource = path_params[1]
        if '?' in resource:
            param = resource.split('?')[1]
            resource = resource.split('?')[0]
            pair = param.split('=')
            key = pair[0]
            value = pair[1]
            return (resource, key, value)
        else:
            id = None
            try:
                id = int(path_params[2])
            except (IndexError, ValueError):
                pass
            return (resource, id)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Handle Get requests to the server"""
        self._set_headers(200)
        response = {}
        parsed = self.parse_url()
        (resource, id) = parsed

        if resource == "users":
            response = get_all_users()
            # turn dict into json string to send
        if resource == "categories":
            response = get_all_categories()

        if resource == "posts":
            posts = get_all_posts()
            response = [post.__dict__ for post in posts]

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        response = ''
        resource, _ = self.parse_url()

        if resource == 'login':
            response = login_user(post_body)
        if resource == 'register':
            response = create_user(post_body)

        if resource == 'categories':
            response = create_category(post_body)

        if resource == "posts":
            create_post(
                user_id=post_body['user_id'],
                category_id=post_body['category_id'],
                title=post_body['title'],
                publication_date=post_body['publication_date'],
                image_url=post_body['image_url'],
                content=post_body['content'],
                approved=post_body['approved']
            )
            response = json.dumps({"message": "Post created"})


        self.wfile.write(response.encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""

        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        resource, id = self.parse_url()

        if resource == "categories":
            success = update_category(id, post_body)

        if resource == "posts":
            update_post(
                post_id=id,
                user_id=post_body['user_id'],
                category_id=post_body['category_id'],
                title=post_body['title'],
                publication_date=post_body['publication_date'],
                image_url=post_body['image_url'],
                content=post_body['content'],
                approved=post_body['approved']
            )

        if resource == "users":
            # will return either True or False from `update_animal`
            success = update_user(id, post_body)

        # handle the value of success
        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)


    def do_DELETE(self):
        """Handle DELETE Requests"""
        #  Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url()

        # Delete a single user from the list
        if resource == "users":
            delete_user(id)
        elif resource == "posts":
            delete_post(id)
        if resource == "categories":
            delete_category(id)

        # Encode the new user and send in response
        self.wfile.write("".encode())


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
