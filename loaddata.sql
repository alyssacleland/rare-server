CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY("admin_id") REFERENCES "Users"("id"),
  FOREIGN KEY("approver_one_id") REFERENCES "Users"("id"),
  PRIMARY KEY ("action", "admin_id", "approver_one_id")
);

CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY("follower_id") REFERENCES "Users"("id"),
  FOREIGN KEY("author_id") REFERENCES "Users"("id")
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,

  FOREIGN KEY("user_id") REFERENCES "Users"("id")
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY("post_id") REFERENCES "Posts"("id"),
  FOREIGN KEY("author_id") REFERENCES "Users"("id")
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY("user_id") REFERENCES "Users"("id"),
  FOREIGN KEY("reaction_id") REFERENCES "Reactions"("id"),
  FOREIGN KEY("post_id") REFERENCES "Posts"("id")
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY("post_id") REFERENCES "Posts"("id"),
  FOREIGN KEY("tag_id") REFERENCES "Tags"("id")
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');

SELECT name FROM sqlite_master WHERE type='table';

select * from Users

INSERT INTO Users ('first_name', 'last_name', 'email', 'bio', 'username', 'password', 'profile_image_url', 'created_on', 'active') VALUES ('Alyssa', 'Cleland', 'alyssamariecleland@gmail.com', 'Alyssa Cleland is a software engineer with a passion for web development and a knack for problem-solving. She enjoys creating user-friendly applications and is always eager to learn new technologies.', 'alyssacleland', 'password123', 'https://example.com/alyssa.jpg', '2023-10-01', 1), 
('Jordan', 'Lee', 'jordanlee@example.com', 'Jordan is a full-stack developer with a love for APIs and clean code.', 'jordanlee', 'passw0rd!', 'https://example.com/jordan.jpg', '2023-10-05', 1),
('Ravi', 'Patel', 'ravi.patel@example.com', 'Ravi specializes in frontend development and has a background in graphic design.', 'ravipatel', 'ravi1234', 'https://example.com/ravi.jpg', '2023-10-06', 1),
('Maria', 'Gomez', 'maria.gomez@example.com', 'Maria is a backend engineer who enjoys building scalable systems and mentoring junior developers.', 'mariagomez', 'securepass', 'https://example.com/maria.jpg', '2023-10-08', 1),
('Chen', 'Wei', 'chen.wei@example.com', 'Chen is a DevOps engineer focused on cloud infrastructure and CI/CD pipelines.', 'chenwei', 'cloudyday', 'https://example.com/chen.jpg', '2023-10-10', 1),
('Amara', 'Jones', 'amara.jones@example.com', 'Amara is a data scientist who bridges the gap between data and business insights.', 'amaraj', 'datasmart', 'https://example.com/amara.jpg', '2023-10-12', 0);

