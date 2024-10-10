PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO django_migrations VALUES(1,'contenttypes','0001_initial','2024-05-12 21:58:08.482496');
INSERT INTO django_migrations VALUES(2,'auth','0001_initial','2024-05-12 21:58:08.491882');
INSERT INTO django_migrations VALUES(3,'admin','0001_initial','2024-05-12 21:58:08.494519');
INSERT INTO django_migrations VALUES(4,'admin','0002_logentry_remove_auto_add','2024-05-12 21:58:08.497118');
INSERT INTO django_migrations VALUES(5,'admin','0003_logentry_add_action_flag_choices','2024-05-12 21:58:08.498933');
INSERT INTO django_migrations VALUES(6,'contenttypes','0002_remove_content_type_name','2024-05-12 21:58:08.502773');
INSERT INTO django_migrations VALUES(7,'auth','0002_alter_permission_name_max_length','2024-05-12 21:58:08.505440');
INSERT INTO django_migrations VALUES(8,'auth','0003_alter_user_email_max_length','2024-05-12 21:58:08.508118');
INSERT INTO django_migrations VALUES(9,'auth','0004_alter_user_username_opts','2024-05-12 21:58:08.509792');
INSERT INTO django_migrations VALUES(10,'auth','0005_alter_user_last_login_null','2024-05-12 21:58:08.511915');
INSERT INTO django_migrations VALUES(11,'auth','0006_require_contenttypes_0002','2024-05-12 21:58:08.512608');
INSERT INTO django_migrations VALUES(12,'auth','0007_alter_validators_add_error_messages','2024-05-12 21:58:08.514110');
INSERT INTO django_migrations VALUES(13,'auth','0008_alter_user_username_max_length','2024-05-12 21:58:08.516386');
INSERT INTO django_migrations VALUES(14,'auth','0009_alter_user_last_name_max_length','2024-05-12 21:58:08.518457');
INSERT INTO django_migrations VALUES(15,'auth','0010_alter_group_name_max_length','2024-05-12 21:58:08.520434');
INSERT INTO django_migrations VALUES(16,'auth','0011_update_proxy_permissions','2024-05-12 21:58:08.522522');
INSERT INTO django_migrations VALUES(17,'auth','0012_alter_user_first_name_max_length','2024-05-12 21:58:08.524784');
INSERT INTO django_migrations VALUES(18,'catalog','0001_initial','2024-05-12 21:58:08.542253');
INSERT INTO django_migrations VALUES(19,'sessions','0001_initial','2024-05-12 21:58:08.543402');
INSERT INTO django_migrations VALUES(20,'catalog','0002_alter_lessondetails_status','2024-05-13 08:30:46.889740');
INSERT INTO django_migrations VALUES(21,'catalog','0003_alter_lessondetails_homework_and_more','2024-05-13 08:36:46.155412');
INSERT INTO django_migrations VALUES(22,'catalog','0004_alter_lesson_duration','2024-05-13 11:05:10.219316');
INSERT INTO django_migrations VALUES(23,'catalog','0005_alter_lesson_duration','2024-05-13 15:49:25.681415');
INSERT INTO django_migrations VALUES(24,'catalog','0006_remove_lessondetails_status_lessonstatus','2024-05-14 16:35:56.126529');
INSERT INTO django_migrations VALUES(25,'catalog','0007_alter_lessonstatus_status','2024-05-14 21:22:26.200064');
INSERT INTO django_migrations VALUES(26,'catalog','0008_alter_studentsattendance_student','2024-05-15 08:38:52.487750');
INSERT INTO django_migrations VALUES(27,'catalog','0009_alter_studentsattendance_student','2024-05-15 09:24:50.742684');
INSERT INTO django_migrations VALUES(28,'catalog','0010_rename_student_studentsattendance_students','2024-05-15 09:49:43.297444');
INSERT INTO django_migrations VALUES(29,'catalog','0011_rename_lessondetails_lessoninfo','2024-05-16 00:54:30.750987');
INSERT INTO django_migrations VALUES(30,'catalog','0012_alter_lessoninfo_homework_alter_lessoninfo_notes_and_more','2024-05-16 14:27:20.962115');
INSERT INTO django_migrations VALUES(31,'catalog','0013_alter_lessoncancel_reason','2024-05-16 20:07:28.896909');
INSERT INTO django_migrations VALUES(32,'catalog','0014_lessoninfo_materials','2024-10-05 22:03:55.017853');
CREATE TABLE IF NOT EXISTS "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_time" datetime NOT NULL);
INSERT INTO django_admin_log VALUES(1,'1','ОГЭ',1,'[{"added": {}}]',10,1,'2024-05-12 23:27:06.624061');
INSERT INTO django_admin_log VALUES(2,'2','ЕГЭ',1,'[{"added": {}}]',10,1,'2024-05-12 23:27:14.688097');
INSERT INTO django_admin_log VALUES(3,'3','школьная прогрпмма 5-9',1,'[{"added": {}}]',10,1,'2024-05-12 23:27:32.397949');
INSERT INTO django_admin_log VALUES(4,'4','школьная программа 10-11',1,'[{"added": {}}]',10,1,'2024-05-12 23:27:47.895101');
INSERT INTO django_admin_log VALUES(5,'5','олимпиады 5-9',1,'[{"added": {}}]',10,1,'2024-05-12 23:28:05.066518');
INSERT INTO django_admin_log VALUES(6,'6','олимпиады 10-11',1,'[{"added": {}}]',10,1,'2024-05-12 23:28:13.873001');
INSERT INTO django_admin_log VALUES(7,'1','математика',1,'[{"added": {}}]',9,1,'2024-05-12 23:28:28.037162');
INSERT INTO django_admin_log VALUES(8,'2','информатика',1,'[{"added": {}}]',9,1,'2024-05-12 23:28:33.868047');
INSERT INTO django_admin_log VALUES(9,'3','физика',1,'[{"added": {}}]',9,1,'2024-05-12 23:28:38.686455');
INSERT INTO django_admin_log VALUES(10,'4','химия',1,'[{"added": {}}]',9,1,'2024-05-12 23:28:43.999640');
INSERT INTO django_admin_log VALUES(11,'5','русский язык',1,'[{"added": {}}]',9,1,'2024-05-12 23:28:52.681817');
INSERT INTO django_admin_log VALUES(12,'6','литература',1,'[{"added": {}}]',9,1,'2024-05-12 23:28:59.432324');
INSERT INTO django_admin_log VALUES(13,'7','английский язык',1,'[{"added": {}}]',9,1,'2024-05-12 23:29:07.034841');
INSERT INTO django_admin_log VALUES(14,'8','история',1,'[{"added": {}}]',9,1,'2024-05-12 23:29:31.049919');
INSERT INTO django_admin_log VALUES(15,'9','обществознание',1,'[{"added": {}}]',9,1,'2024-05-12 23:29:37.502444');
INSERT INTO django_admin_log VALUES(16,'10','география',1,'[{"added": {}}]',9,1,'2024-05-12 23:29:47.449773');
INSERT INTO django_admin_log VALUES(17,'11','биология',1,'[{"added": {}}]',9,1,'2024-05-12 23:29:51.832035');
INSERT INTO django_admin_log VALUES(18,'2','Новикова Вероника',1,'[{"added": {}}]',8,1,'2024-05-12 23:40:50.790387');
INSERT INTO django_admin_log VALUES(19,'3','Бурнышева Алина',1,'[{"added": {}}]',8,1,'2024-05-12 23:42:34.952533');
INSERT INTO django_admin_log VALUES(20,'4','Самаева Ева',1,'[{"added": {}}]',8,1,'2024-05-12 23:47:23.000961');
INSERT INTO django_admin_log VALUES(21,'5','Кондохов Марк',1,'[{"added": {}}]',8,1,'2024-05-12 23:48:25.163294');
INSERT INTO django_admin_log VALUES(22,'1','Виктория',1,'[{"added": {}}]',16,1,'2024-05-12 23:51:06.191592');
INSERT INTO django_admin_log VALUES(23,'2','Анастасия',1,'[{"added": {}}]',16,1,'2024-05-12 23:52:40.448141');
INSERT INTO django_admin_log VALUES(24,'3','Виталий',1,'[{"added": {}}]',16,1,'2024-05-12 23:54:31.715472');
INSERT INTO django_admin_log VALUES(25,'3','Lesson object (3)',1,'[{"added": {}}]',11,1,'2024-05-13 11:16:05.330861');
INSERT INTO django_admin_log VALUES(26,'3','Lesson object (3)',3,'',11,1,'2024-05-13 15:48:34.215806');
INSERT INTO django_admin_log VALUES(27,'5','Lesson object (5)',3,'',11,1,'2024-05-14 22:34:36.844591');
INSERT INTO django_admin_log VALUES(28,'4','Lesson object (4)',3,'',11,1,'2024-05-14 22:34:41.442037');
INSERT INTO django_admin_log VALUES(29,'3','Lesson object (3)',3,'',11,1,'2024-05-14 22:34:44.624579');
INSERT INTO django_admin_log VALUES(30,'2','Lesson object (2)',3,'',11,1,'2024-05-14 22:34:48.776719');
INSERT INTO django_admin_log VALUES(31,'6','Lesson object (6)',3,'',11,1,'2024-05-14 22:34:54.059268');
INSERT INTO django_admin_log VALUES(32,'1','Lesson object (1)',3,'',11,1,'2024-05-14 22:34:56.958795');
CREATE TABLE IF NOT EXISTS "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
INSERT INTO django_content_type VALUES(1,'admin','logentry');
INSERT INTO django_content_type VALUES(2,'auth','permission');
INSERT INTO django_content_type VALUES(3,'auth','group');
INSERT INTO django_content_type VALUES(4,'auth','user');
INSERT INTO django_content_type VALUES(5,'contenttypes','contenttype');
INSERT INTO django_content_type VALUES(6,'sessions','session');
INSERT INTO django_content_type VALUES(7,'catalog','group');
INSERT INTO django_content_type VALUES(8,'catalog','student');
INSERT INTO django_content_type VALUES(9,'catalog','subject');
INSERT INTO django_content_type VALUES(10,'catalog','type');
INSERT INTO django_content_type VALUES(11,'catalog','lesson');
INSERT INTO django_content_type VALUES(12,'catalog','lessoninfo');
INSERT INTO django_content_type VALUES(13,'catalog','students_in_group');
INSERT INTO django_content_type VALUES(14,'catalog','studentsattendance');
INSERT INTO django_content_type VALUES(15,'catalog','student_subjects');
INSERT INTO django_content_type VALUES(16,'catalog','worker');
INSERT INTO django_content_type VALUES(17,'catalog','lessonstatus');
INSERT INTO django_content_type VALUES(18,'catalog','lessoncancel');
CREATE TABLE IF NOT EXISTS "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
INSERT INTO auth_permission VALUES(1,1,'add_logentry','Can add log entry');
INSERT INTO auth_permission VALUES(2,1,'change_logentry','Can change log entry');
INSERT INTO auth_permission VALUES(3,1,'delete_logentry','Can delete log entry');
INSERT INTO auth_permission VALUES(4,1,'view_logentry','Can view log entry');
INSERT INTO auth_permission VALUES(5,2,'add_permission','Can add permission');
INSERT INTO auth_permission VALUES(6,2,'change_permission','Can change permission');
INSERT INTO auth_permission VALUES(7,2,'delete_permission','Can delete permission');
INSERT INTO auth_permission VALUES(8,2,'view_permission','Can view permission');
INSERT INTO auth_permission VALUES(9,3,'add_group','Can add group');
INSERT INTO auth_permission VALUES(10,3,'change_group','Can change group');
INSERT INTO auth_permission VALUES(11,3,'delete_group','Can delete group');
INSERT INTO auth_permission VALUES(12,3,'view_group','Can view group');
INSERT INTO auth_permission VALUES(13,4,'add_user','Can add user');
INSERT INTO auth_permission VALUES(14,4,'change_user','Can change user');
INSERT INTO auth_permission VALUES(15,4,'delete_user','Can delete user');
INSERT INTO auth_permission VALUES(16,4,'view_user','Can view user');
INSERT INTO auth_permission VALUES(17,5,'add_contenttype','Can add content type');
INSERT INTO auth_permission VALUES(18,5,'change_contenttype','Can change content type');
INSERT INTO auth_permission VALUES(19,5,'delete_contenttype','Can delete content type');
INSERT INTO auth_permission VALUES(20,5,'view_contenttype','Can view content type');
INSERT INTO auth_permission VALUES(21,6,'add_session','Can add session');
INSERT INTO auth_permission VALUES(22,6,'change_session','Can change session');
INSERT INTO auth_permission VALUES(23,6,'delete_session','Can delete session');
INSERT INTO auth_permission VALUES(24,6,'view_session','Can view session');
INSERT INTO auth_permission VALUES(25,7,'add_group','Can add group');
INSERT INTO auth_permission VALUES(26,7,'change_group','Can change group');
INSERT INTO auth_permission VALUES(27,7,'delete_group','Can delete group');
INSERT INTO auth_permission VALUES(28,7,'view_group','Can view group');
INSERT INTO auth_permission VALUES(29,8,'add_student','Can add student');
INSERT INTO auth_permission VALUES(30,8,'change_student','Can change student');
INSERT INTO auth_permission VALUES(31,8,'delete_student','Can delete student');
INSERT INTO auth_permission VALUES(32,8,'view_student','Can view student');
INSERT INTO auth_permission VALUES(33,9,'add_subject','Can add subject');
INSERT INTO auth_permission VALUES(34,9,'change_subject','Can change subject');
INSERT INTO auth_permission VALUES(35,9,'delete_subject','Can delete subject');
INSERT INTO auth_permission VALUES(36,9,'view_subject','Can view subject');
INSERT INTO auth_permission VALUES(37,10,'add_type','Can add type');
INSERT INTO auth_permission VALUES(38,10,'change_type','Can change type');
INSERT INTO auth_permission VALUES(39,10,'delete_type','Can delete type');
INSERT INTO auth_permission VALUES(40,10,'view_type','Can view type');
INSERT INTO auth_permission VALUES(41,11,'add_lesson','Can add lesson');
INSERT INTO auth_permission VALUES(42,11,'change_lesson','Can change lesson');
INSERT INTO auth_permission VALUES(43,11,'delete_lesson','Can delete lesson');
INSERT INTO auth_permission VALUES(44,11,'view_lesson','Can view lesson');
INSERT INTO auth_permission VALUES(45,12,'add_lessondetails','Can add lesson details');
INSERT INTO auth_permission VALUES(46,12,'change_lessondetails','Can change lesson details');
INSERT INTO auth_permission VALUES(47,12,'delete_lessondetails','Can delete lesson details');
INSERT INTO auth_permission VALUES(48,12,'view_lessondetails','Can view lesson details');
INSERT INTO auth_permission VALUES(49,13,'add_students_in_group','Can add students_in_group');
INSERT INTO auth_permission VALUES(50,13,'change_students_in_group','Can change students_in_group');
INSERT INTO auth_permission VALUES(51,13,'delete_students_in_group','Can delete students_in_group');
INSERT INTO auth_permission VALUES(52,13,'view_students_in_group','Can view students_in_group');
INSERT INTO auth_permission VALUES(53,14,'add_studentsattendance','Can add students attendance');
INSERT INTO auth_permission VALUES(54,14,'change_studentsattendance','Can change students attendance');
INSERT INTO auth_permission VALUES(55,14,'delete_studentsattendance','Can delete students attendance');
INSERT INTO auth_permission VALUES(56,14,'view_studentsattendance','Can view students attendance');
INSERT INTO auth_permission VALUES(57,15,'add_student_subjects','Can add student_ subjects');
INSERT INTO auth_permission VALUES(58,15,'change_student_subjects','Can change student_ subjects');
INSERT INTO auth_permission VALUES(59,15,'delete_student_subjects','Can delete student_ subjects');
INSERT INTO auth_permission VALUES(60,15,'view_student_subjects','Can view student_ subjects');
INSERT INTO auth_permission VALUES(61,16,'add_worker','Can add worker');
INSERT INTO auth_permission VALUES(62,16,'change_worker','Can change worker');
INSERT INTO auth_permission VALUES(63,16,'delete_worker','Can delete worker');
INSERT INTO auth_permission VALUES(64,16,'view_worker','Can view worker');
INSERT INTO auth_permission VALUES(65,17,'add_lessonstatus','Can add lesson status');
INSERT INTO auth_permission VALUES(66,17,'change_lessonstatus','Can change lesson status');
INSERT INTO auth_permission VALUES(67,17,'delete_lessonstatus','Can delete lesson status');
INSERT INTO auth_permission VALUES(68,17,'view_lessonstatus','Can view lesson status');
INSERT INTO auth_permission VALUES(69,12,'add_lessoninfo','Can add lesson info');
INSERT INTO auth_permission VALUES(70,12,'change_lessoninfo','Can change lesson info');
INSERT INTO auth_permission VALUES(71,12,'delete_lessoninfo','Can delete lesson info');
INSERT INTO auth_permission VALUES(72,12,'view_lessoninfo','Can view lesson info');
INSERT INTO auth_permission VALUES(73,18,'add_lessoncancel','Can add lesson cancel');
INSERT INTO auth_permission VALUES(74,18,'change_lessoncancel','Can change lesson cancel');
INSERT INTO auth_permission VALUES(75,18,'delete_lessoncancel','Can delete lesson cancel');
INSERT INTO auth_permission VALUES(76,18,'view_lessoncancel','Can view lesson cancel');
CREATE TABLE IF NOT EXISTS "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "first_name" varchar(150) NOT NULL);
INSERT INTO auth_user VALUES(1,'pbkdf2_sha256$720000$QfYDG7w6twwC70Ta9MGTdc$UU2zz8fydiunPFAdZwtmdNBuuE6WEItYOGsablePlKg=','2024-05-12 23:26:28.586604',1,'fursatora','','',1,1,'2024-05-12 23:24:40.515681','');
CREATE TABLE IF NOT EXISTS "catalog_student" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "firstname" varchar(20) NOT NULL, "lastname" varchar(20) NOT NULL, "fathername" varchar(20) NOT NULL, "date_of_birth" date NOT NULL, "grade" integer NOT NULL, "phone_number" varchar(11) NOT NULL, "email" varchar(254) NOT NULL);
INSERT INTO catalog_student VALUES(1,'Максим','Гаврилов','Владимирович','2002-08-28',10,'89788214859','mega.max.1@gmail.com');
INSERT INTO catalog_student VALUES(2,'Вероника','Новикова','Сергеевна','2003-12-20',10,'89675436756','nov@gmail.com');
INSERT INTO catalog_student VALUES(3,'Алина','Бурнышева','Александровна','2004-03-23',9,'89873245671','alinchik@yandex.ru');
INSERT INTO catalog_student VALUES(4,'Ева','Самаева','Григорьевна','2008-09-15',7,'84567436547','eva@mail.ru');
INSERT INTO catalog_student VALUES(5,'Марк','Кондохов','Алексеевич','2006-07-20',7,'86543265884','markiz@gmail.com');
CREATE TABLE IF NOT EXISTS "catalog_subject" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL);
INSERT INTO catalog_subject VALUES(1,'математика');
INSERT INTO catalog_subject VALUES(2,'информатика');
INSERT INTO catalog_subject VALUES(3,'физика');
INSERT INTO catalog_subject VALUES(4,'химия');
INSERT INTO catalog_subject VALUES(5,'русский язык');
INSERT INTO catalog_subject VALUES(6,'литература');
INSERT INTO catalog_subject VALUES(7,'английский язык');
INSERT INTO catalog_subject VALUES(8,'история');
INSERT INTO catalog_subject VALUES(9,'обществознание');
INSERT INTO catalog_subject VALUES(10,'география');
INSERT INTO catalog_subject VALUES(11,'биология');
CREATE TABLE IF NOT EXISTS "catalog_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL);
INSERT INTO catalog_type VALUES(1,'ОГЭ');
INSERT INTO catalog_type VALUES(2,'ЕГЭ');
INSERT INTO catalog_type VALUES(3,'школьная прогрпмма 5-9');
INSERT INTO catalog_type VALUES(4,'школьная программа 10-11');
INSERT INTO catalog_type VALUES(5,'олимпиады 5-9');
INSERT INTO catalog_type VALUES(6,'олимпиады 10-11');
CREATE TABLE IF NOT EXISTS "catalog_students_in_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" bigint NOT NULL REFERENCES "catalog_group" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO catalog_students_in_group VALUES(1,1);
INSERT INTO catalog_students_in_group VALUES(2,2);
INSERT INTO catalog_students_in_group VALUES(3,3);
INSERT INTO catalog_students_in_group VALUES(4,5);
INSERT INTO catalog_students_in_group VALUES(6,10);
INSERT INTO catalog_students_in_group VALUES(9,8);
INSERT INTO catalog_students_in_group VALUES(10,13);
INSERT INTO catalog_students_in_group VALUES(14,14);
INSERT INTO catalog_students_in_group VALUES(20,20);
CREATE TABLE IF NOT EXISTS "catalog_students_in_group_student" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "students_in_group_id" bigint NOT NULL REFERENCES "catalog_students_in_group" ("id") DEFERRABLE INITIALLY DEFERRED, "student_id" bigint NOT NULL REFERENCES "catalog_student" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO catalog_students_in_group_student VALUES(1,1,1);
INSERT INTO catalog_students_in_group_student VALUES(2,1,2);
INSERT INTO catalog_students_in_group_student VALUES(3,2,1);
INSERT INTO catalog_students_in_group_student VALUES(4,2,3);
INSERT INTO catalog_students_in_group_student VALUES(5,2,4);
INSERT INTO catalog_students_in_group_student VALUES(6,3,1);
INSERT INTO catalog_students_in_group_student VALUES(7,4,1);
INSERT INTO catalog_students_in_group_student VALUES(8,4,3);
INSERT INTO catalog_students_in_group_student VALUES(9,4,4);
INSERT INTO catalog_students_in_group_student VALUES(10,4,5);
INSERT INTO catalog_students_in_group_student VALUES(11,6,4);
INSERT INTO catalog_students_in_group_student VALUES(12,6,5);
INSERT INTO catalog_students_in_group_student VALUES(13,10,1);
INSERT INTO catalog_students_in_group_student VALUES(14,14,3);
CREATE TABLE IF NOT EXISTS "catalog_studentsattendance" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "lesson_id" bigint NOT NULL REFERENCES "catalog_lesson" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO catalog_studentsattendance VALUES(8,10);
INSERT INTO catalog_studentsattendance VALUES(11,7);
INSERT INTO catalog_studentsattendance VALUES(12,11);
INSERT INTO catalog_studentsattendance VALUES(13,8);
INSERT INTO catalog_studentsattendance VALUES(14,12);
INSERT INTO catalog_studentsattendance VALUES(15,14);
CREATE TABLE IF NOT EXISTS "catalog_student_subjects" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "student_id" bigint NOT NULL REFERENCES "catalog_student" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO catalog_student_subjects VALUES(1,1);
INSERT INTO catalog_student_subjects VALUES(2,5);
INSERT INTO catalog_student_subjects VALUES(3,3);
INSERT INTO catalog_student_subjects VALUES(4,4);
INSERT INTO catalog_student_subjects VALUES(5,2);
CREATE TABLE IF NOT EXISTS "catalog_student_subjects_subjects" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "student_subjects_id" bigint NOT NULL REFERENCES "catalog_student_subjects" ("id") DEFERRABLE INITIALLY DEFERRED, "subject_id" bigint NOT NULL REFERENCES "catalog_subject" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO catalog_student_subjects_subjects VALUES(1,1,1);
INSERT INTO catalog_student_subjects_subjects VALUES(2,1,10);
INSERT INTO catalog_student_subjects_subjects VALUES(3,1,5);
INSERT INTO catalog_student_subjects_subjects VALUES(4,2,1);
INSERT INTO catalog_student_subjects_subjects VALUES(5,2,5);
INSERT INTO catalog_student_subjects_subjects VALUES(6,2,7);
INSERT INTO catalog_student_subjects_subjects VALUES(7,3,9);
INSERT INTO catalog_student_subjects_subjects VALUES(8,3,5);
INSERT INTO catalog_student_subjects_subjects VALUES(9,3,6);
INSERT INTO catalog_student_subjects_subjects VALUES(10,4,1);
INSERT INTO catalog_student_subjects_subjects VALUES(11,4,3);
INSERT INTO catalog_student_subjects_subjects VALUES(12,4,5);
INSERT INTO catalog_student_subjects_subjects VALUES(13,4,7);
INSERT INTO catalog_student_subjects_subjects VALUES(14,5,1);
INSERT INTO catalog_student_subjects_subjects VALUES(15,5,2);
INSERT INTO catalog_student_subjects_subjects VALUES(16,5,3);
INSERT INTO catalog_student_subjects_subjects VALUES(17,5,4);
CREATE TABLE IF NOT EXISTS "catalog_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "grade" integer NOT NULL, "group_capacity" integer NOT NULL, "created" bool NOT NULL, "subject_id" bigint NOT NULL REFERENCES "catalog_subject" ("id") DEFERRABLE INITIALLY DEFERRED, "type_id" bigint NOT NULL REFERENCES "catalog_type" ("id") DEFERRABLE INITIALLY DEFERRED, "teacher_id" bigint NULL REFERENCES "catalog_worker" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO catalog_group VALUES(1,10,3,0,1,2,1);
INSERT INTO catalog_group VALUES(2,9,5,0,5,1,2);
INSERT INTO catalog_group VALUES(3,5,5,0,10,2,4);
INSERT INTO catalog_group VALUES(5,5,4,0,5,3,2);
INSERT INTO catalog_group VALUES(8,8,6,0,7,3,2);
INSERT INTO catalog_group VALUES(10,8,6,0,7,3,2);
INSERT INTO catalog_group VALUES(13,1,1,0,1,1,3);
INSERT INTO catalog_group VALUES(14,1,1,0,5,1,2);
INSERT INTO catalog_group VALUES(20,9,3,0,7,1,3);
CREATE TABLE IF NOT EXISTS "catalog_worker" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "firstname" varchar(20) NOT NULL, "lastname" varchar(20) NOT NULL, "fathername" varchar(20) NOT NULL, "date_of_birth" date NOT NULL, "gender" integer NOT NULL, "phone_number" varchar(11) NOT NULL, "email" varchar(254) NOT NULL, "registration_date" date NOT NULL);
INSERT INTO catalog_worker VALUES(1,'Виктория','Фурса','Евгеньевна','2004-02-21',0,'89788214859','vikahomeacc@gmail.com','2024-05-13');
INSERT INTO catalog_worker VALUES(2,'Анастасия','Петрусевич','Ивановна','2002-12-21',0,'89785437444','aaaa@gmail.com','2024-05-13');
INSERT INTO catalog_worker VALUES(3,'Виталий','Гиндес','Максимович','2000-03-02',1,'89183455432','vitalino@yandex.ru','2024-05-18');
INSERT INTO catalog_worker VALUES(4,'Ирина','Гриц','Александровна','1984-09-07',0,'87654538723','irina@mail.ru','2024-05-15');
CREATE TABLE IF NOT EXISTS "catalog_worker_subject" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "worker_id" bigint NOT NULL REFERENCES "catalog_worker" ("id") DEFERRABLE INITIALLY DEFERRED, "subject_id" bigint NOT NULL REFERENCES "catalog_subject" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO catalog_worker_subject VALUES(1,1,1);
INSERT INTO catalog_worker_subject VALUES(2,1,2);
INSERT INTO catalog_worker_subject VALUES(3,2,5);
INSERT INTO catalog_worker_subject VALUES(4,2,6);
INSERT INTO catalog_worker_subject VALUES(5,2,7);
INSERT INTO catalog_worker_subject VALUES(9,4,10);
INSERT INTO catalog_worker_subject VALUES(13,3,8);
INSERT INTO catalog_worker_subject VALUES(14,3,9);
INSERT INTO catalog_worker_subject VALUES(15,3,7);
CREATE TABLE IF NOT EXISTS "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
INSERT INTO django_session VALUES('r30dhwfdtvibssgjpp29by0o9ouk1h3i','.eJxVjMsOwiAUBf-FtSEWeim4dN9vIPcBUjU0Ke3K-O_apAvdnpk5LxVxW0vcWlriJOqiOnX63Qj5keoO5I71Nmue67pMpHdFH7TpcZb0vB7u30HBVr51RhTOYDw6lgRBhIeM1joI2JM3Qwg9GZ_JMxFZQc_inTlbAxk6EPX-ACLdOP4:1s6IaK:GfoOhq92wdefS9iZPGFxvFcnqUcENUNNXeSXMlyUPjM','2024-05-26 23:26:28.587779');
CREATE TABLE IF NOT EXISTS "catalog_lesson" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "date" date NOT NULL, "start_time" datetime NOT NULL, "group_id" bigint NOT NULL REFERENCES "catalog_group" ("id") DEFERRABLE INITIALLY DEFERRED, "duration" integer NOT NULL);
INSERT INTO catalog_lesson VALUES(7,'2024-05-09','2024-05-09 05:00:00',2,2);
INSERT INTO catalog_lesson VALUES(8,'2024-05-12','2024-05-12 11:00:00',2,1);
INSERT INTO catalog_lesson VALUES(10,'2024-06-01','2024-06-01 05:00:00',2,2);
INSERT INTO catalog_lesson VALUES(11,'2024-05-28','2024-05-28 16:00:00',3,1);
INSERT INTO catalog_lesson VALUES(12,'2024-05-17','2024-05-17 12:00:00',1,1);
INSERT INTO catalog_lesson VALUES(13,'2024-07-01','2024-07-01 09:00:00',1,1);
INSERT INTO catalog_lesson VALUES(14,'2024-05-14','2024-05-14 15:00:00',1,1);
INSERT INTO catalog_lesson VALUES(16,'2024-05-18','2024-05-18 13:00:00',20,2);
CREATE TABLE IF NOT EXISTS "catalog_lessonstatus" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "lesson_id" bigint NOT NULL REFERENCES "catalog_lesson" ("id") DEFERRABLE INITIALLY DEFERRED, "status" integer NULL);
INSERT INTO catalog_lessonstatus VALUES(3,7,1);
INSERT INTO catalog_lessonstatus VALUES(4,8,1);
INSERT INTO catalog_lessonstatus VALUES(6,10,1);
INSERT INTO catalog_lessonstatus VALUES(7,11,0);
INSERT INTO catalog_lessonstatus VALUES(8,12,1);
INSERT INTO catalog_lessonstatus VALUES(9,13,0);
INSERT INTO catalog_lessonstatus VALUES(10,14,1);
INSERT INTO catalog_lessonstatus VALUES(12,16,3);
CREATE TABLE IF NOT EXISTS "catalog_studentsattendance_students" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "studentsattendance_id" bigint NOT NULL REFERENCES "catalog_studentsattendance" ("id") DEFERRABLE INITIALLY DEFERRED, "student_id" bigint NOT NULL REFERENCES "catalog_student" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO catalog_studentsattendance_students VALUES(11,8,3);
INSERT INTO catalog_studentsattendance_students VALUES(12,8,4);
INSERT INTO catalog_studentsattendance_students VALUES(15,11,1);
INSERT INTO catalog_studentsattendance_students VALUES(17,11,4);
INSERT INTO catalog_studentsattendance_students VALUES(19,13,3);
INSERT INTO catalog_studentsattendance_students VALUES(20,13,4);
INSERT INTO catalog_studentsattendance_students VALUES(21,14,1);
INSERT INTO catalog_studentsattendance_students VALUES(22,14,2);
INSERT INTO catalog_studentsattendance_students VALUES(23,13,1);
INSERT INTO catalog_studentsattendance_students VALUES(24,15,1);
INSERT INTO catalog_studentsattendance_students VALUES(26,15,2);
CREATE TABLE IF NOT EXISTS "catalog_lessoninfo" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "homework" text NULL, "notes" text NULL, "lesson_id" bigint NOT NULL REFERENCES "catalog_lesson" ("id") DEFERRABLE INITIALLY DEFERRED, "topic" text NULL, "materials" varchar(200) NULL);
INSERT INTO catalog_lessoninfo VALUES(1,'учить теорему Пифагора','Гаврилову Максиму сделано замечание',7,'Причастный оборот','https://storage.yandexcloud.net/studycenter/%D1%8D%D0%BA%D0%BE%D0%BD%D1%80%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%D0%BA%D0%BB%D0%B0%D1%81%D1%812.docx');
INSERT INTO catalog_lessoninfo VALUES(2,'учиться','учились',12,'Теорема Пифагора',NULL);
INSERT INTO catalog_lessoninfo VALUES(3,'-','-',8,'Теорема Пифагора','https://storage.yandexcloud.net/studycenter/%D1%8D%D0%BA%D0%BE%D0%BD%D1%80%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5%D0%BA%D0%BB%D0%B0%D1%81%D1%812.docx');
INSERT INTO catalog_lessoninfo VALUES(4,'Сборник Ященко: задание 13 в вариантах 10-22','На следующем занятии самостоятельная по простейшим тригонометрическим уравнениям',14,'Разбор №13. Тригоноетрические уравнения',NULL);
CREATE TABLE IF NOT EXISTS "catalog_lessoncancel" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "lesson_id" bigint NOT NULL REFERENCES "catalog_lesson" ("id") DEFERRABLE INITIALLY DEFERRED, "reason" text NULL);
INSERT INTO catalog_lessoncancel VALUES(1,11,'Преподаватель на больничном');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('django_migrations',32);
INSERT INTO sqlite_sequence VALUES('django_admin_log',32);
INSERT INTO sqlite_sequence VALUES('django_content_type',18);
INSERT INTO sqlite_sequence VALUES('auth_permission',76);
INSERT INTO sqlite_sequence VALUES('auth_group',0);
INSERT INTO sqlite_sequence VALUES('auth_user',1);
INSERT INTO sqlite_sequence VALUES('catalog_group',20);
INSERT INTO sqlite_sequence VALUES('catalog_type',6);
INSERT INTO sqlite_sequence VALUES('catalog_subject',11);
INSERT INTO sqlite_sequence VALUES('catalog_student',5);
INSERT INTO sqlite_sequence VALUES('catalog_student_subjects',5);
INSERT INTO sqlite_sequence VALUES('catalog_student_subjects_subjects',17);
INSERT INTO sqlite_sequence VALUES('catalog_worker',4);
INSERT INTO sqlite_sequence VALUES('catalog_worker_subject',15);
INSERT INTO sqlite_sequence VALUES('catalog_students_in_group',20);
INSERT INTO sqlite_sequence VALUES('catalog_students_in_group_student',14);
INSERT INTO sqlite_sequence VALUES('catalog_lesson',16);
INSERT INTO sqlite_sequence VALUES('catalog_lessonstatus',12);
INSERT INTO sqlite_sequence VALUES('catalog_studentsattendance',15);
INSERT INTO sqlite_sequence VALUES('catalog_studentsattendance_students',26);
INSERT INTO sqlite_sequence VALUES('catalog_lessoninfo',4);
INSERT INTO sqlite_sequence VALUES('catalog_lessoncancel',1);
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" ("user_id", "group_id");
CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id");
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE INDEX "catalog_students_in_group_group_id_f19a19ff" ON "catalog_students_in_group" ("group_id");
CREATE UNIQUE INDEX "catalog_students_in_group_student_students_in_group_id_student_id_a9ed6723_uniq" ON "catalog_students_in_group_student" ("students_in_group_id", "student_id");
CREATE INDEX "catalog_students_in_group_student_students_in_group_id_996c1bcf" ON "catalog_students_in_group_student" ("students_in_group_id");
CREATE INDEX "catalog_students_in_group_student_student_id_b0947a9c" ON "catalog_students_in_group_student" ("student_id");
CREATE INDEX "catalog_studentsattendance_lesson_id_420f8df8" ON "catalog_studentsattendance" ("lesson_id");
CREATE INDEX "catalog_student_subjects_student_id_631bde01" ON "catalog_student_subjects" ("student_id");
CREATE UNIQUE INDEX "catalog_student_subjects_subjects_student_subjects_id_subject_id_2cb559a4_uniq" ON "catalog_student_subjects_subjects" ("student_subjects_id", "subject_id");
CREATE INDEX "catalog_student_subjects_subjects_student_subjects_id_dbb75f7f" ON "catalog_student_subjects_subjects" ("student_subjects_id");
CREATE INDEX "catalog_student_subjects_subjects_subject_id_11cdea7e" ON "catalog_student_subjects_subjects" ("subject_id");
CREATE INDEX "catalog_group_subject_id_c8832f8e" ON "catalog_group" ("subject_id");
CREATE INDEX "catalog_group_type_id_3dc47089" ON "catalog_group" ("type_id");
CREATE UNIQUE INDEX "catalog_worker_subject_worker_id_subject_id_92c4a241_uniq" ON "catalog_worker_subject" ("worker_id", "subject_id");
CREATE INDEX "catalog_worker_subject_worker_id_ce082b37" ON "catalog_worker_subject" ("worker_id");
CREATE INDEX "catalog_worker_subject_subject_id_5122802e" ON "catalog_worker_subject" ("subject_id");
CREATE INDEX "catalog_group_teacher_id_74584986" ON "catalog_group" ("teacher_id");
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
CREATE INDEX "catalog_lesson_group_id_124a8d10" ON "catalog_lesson" ("group_id");
CREATE INDEX "catalog_lessonstatus_lesson_id_07376aee" ON "catalog_lessonstatus" ("lesson_id");
CREATE UNIQUE INDEX "catalog_studentsattendance_students_studentsattendance_id_student_id_7745425c_uniq" ON "catalog_studentsattendance_students" ("studentsattendance_id", "student_id");
CREATE INDEX "catalog_studentsattendance_students_studentsattendance_id_c761afde" ON "catalog_studentsattendance_students" ("studentsattendance_id");
CREATE INDEX "catalog_studentsattendance_students_student_id_55ad9165" ON "catalog_studentsattendance_students" ("student_id");
CREATE INDEX "catalog_lessoninfo_lesson_id_d8d17caf" ON "catalog_lessoninfo" ("lesson_id");
CREATE INDEX "catalog_lessoncancel_lesson_id_b6d62d7b" ON "catalog_lessoncancel" ("lesson_id");
COMMIT;
