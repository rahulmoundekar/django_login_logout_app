# django_login_logout_app
django_login_logout_app

### project SQL script as below :

    DROP TABLE IF EXISTS `djangoapp`.`user`;
    CREATE TABLE  `djangoapp`.`user` (
      `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
      `email` varchar(45) NOT NULL,
      `password` varchar(45) NOT NULL,
      `first_name` varchar(45) NOT NULL,
      `last_name` varchar(45) NOT NULL,
      `is_staff` tinyint(1) NOT NULL,
      `is_superuser` tinyint(1) NOT NULL,
      `last_login` datetime NOT NULL,
      `date_joined` datetime NOT NULL,
      `is_active` tinyint(1) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
    
        DROP TABLE IF EXISTS `djangoapp`.`login_user`;
        CREATE TABLE  `djangoapp`.`login_user` (
          `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
          `name` varchar(45) NOT NULL,
          `mobile` varchar(45) NOT NULL,
          `user_id` int(10) unsigned NOT NULL,
          PRIMARY KEY (`id`),
          KEY `FK_staff_1` (`user_id`),
          CONSTRAINT `FK_staff_1` FOREIGN KEY (`user_id`) REFERENCES `login_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
        ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
