/*
SQLyog Professional v12.5.1 (32 bit)
MySQL - 10.1.34-MariaDB : Database - dbbelajarflask
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`dbbelajarflask` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `dbbelajarflask`;

/*Table structure for table `alembic_version` */

DROP TABLE IF EXISTS `alembic_version`;

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `alembic_version` */

insert  into `alembic_version`(`version_num`) values 
('540019bae805');

/*Table structure for table `dosen` */

DROP TABLE IF EXISTS `dosen`;

CREATE TABLE `dosen` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nidn` varchar(30) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `phone` varchar(13) NOT NULL,
  `alamat` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nidn` (`nidn`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `dosen` */

insert  into `dosen`(`id`,`nidn`,`nama`,`phone`,`alamat`) values 
(1,'123456780','Anom','08565656','Janti'),
(2,'123456781','Bekti','08965566','Babarsari'),
(3,'123456782','Ica','08565655','Jrakah');

/*Table structure for table `mahasiswa` */

DROP TABLE IF EXISTS `mahasiswa`;

CREATE TABLE `mahasiswa` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nim` varchar(30) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `phone` varchar(13) NOT NULL,
  `alamat` varchar(100) NOT NULL,
  `dosen_satu` bigint(20) DEFAULT NULL,
  `dosen_dua` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nim` (`nim`),
  KEY `dosen_dua` (`dosen_dua`),
  KEY `dosen_satu` (`dosen_satu`),
  CONSTRAINT `mahasiswa_ibfk_1` FOREIGN KEY (`dosen_dua`) REFERENCES `dosen` (`id`),
  CONSTRAINT `mahasiswa_ibfk_2` FOREIGN KEY (`dosen_satu`) REFERENCES `dosen` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `mahasiswa` */

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(250) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_user_email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
