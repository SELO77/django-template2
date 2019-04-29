CREATE DATABASE IF NOT EXISTS bbakdoc DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE bbakdoc;

-- INSERT INTO `user_dtuser` (`id`, `is_superuser`, `password`, `email`, `is_staff`, `is_active`, `date_joined`, `last_login`, `name`, `phone`, 	`sex`) SELECT 1, 1, 'pbkdf2_sha256$120000$R5eBe2HymL1l$Jg14VWj2O2Hz7YslDPFl+wcoviREKeSnL41GPBBA/Cs=', 'admin@admin.com', 1, 1, '2019-04-28 13:29:53.210076', NULL, 'superuser', '', 1 FROM DUAL
-- WHERE NOT EXISTS (SELECT `email` FROM `user_dtuser` WHERE `email` = 'admin@admin.com');
