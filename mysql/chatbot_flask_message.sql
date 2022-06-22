-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: chatbot_flask
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `message_id` varchar(36) NOT NULL,
  `conversation_id` varchar(36) DEFAULT NULL,
  `message_text` text,
  `sent_time` datetime DEFAULT NULL,
  PRIMARY KEY (`message_id`),
  KEY `conversation_id` (`conversation_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`conversation_id`) REFERENCES `conversation` (`conversation_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES ('18d69bee-f1fb-11ec-a707-50ebf6963744','1cdef58c-aa3c-4c64-84da-ef785e9bb2f8','Chao tam biet','2022-06-22 14:15:29'),('1d333096-f1fa-11ec-a939-50ebf6963744','d9012fdf-7b21-47d4-a49d-1611e4686cc4','Wel come to the hood','2022-06-22 14:08:27'),('431e2468-f1f2-11ec-8f58-50ebf6963744','8eb540df-0fc6-42d5-bf30-12eb8bda5f24','My name jeff','2022-06-22 13:12:15'),('62e8b388-f1f9-11ec-acfa-50ebf6963744','139cb328-c48e-4393-a32d-01dfe691f802','Món này giá bao nhiêu thế?','2022-06-22 14:03:15'),('7a25f8b5-f1f9-11ec-aba6-50ebf6963744','139cb328-c48e-4393-a32d-01dfe691f802','Món này giá bao nhiêu thế?','2022-06-22 14:03:54'),('83c9c78d-f1f9-11ec-82af-50ebf6963744','70fbd32b-b935-4092-9588-2c1e9f50cc1b','This is a robbery','2022-06-22 14:04:10'),('87458887-f1fa-11ec-a5b8-50ebf6963744','83614507-ca49-40ac-a0b7-3d0b3330c768','HAHA dcm thang lz','2022-06-22 14:11:25'),('b6a665a8-f1f6-11ec-ada8-50ebf6963744','8eb540df-0fc6-42d5-bf30-12eb8bda5f24','My name jeff','2022-06-22 13:44:07'),('c23b5c5c-f1ec-11ec-9685-50ebf6963744','8eb540df-0fc6-42d5-bf30-12eb8bda5f24','helloooooo','2022-06-22 12:32:51'),('c4bd10ac-f231-11ec-9d63-50ebf6963744','1cdef58c-aa3c-4c64-84da-ef785e9bb2f8','Chao tam biet','2022-06-22 20:46:50'),('c518eeef-f1f6-11ec-9bfc-50ebf6963744','8eb540df-0fc6-42d5-bf30-12eb8bda5f24','Your mom gae','2022-06-22 13:44:31'),('dd4dbe45-f1f6-11ec-96cf-50ebf6963744','139cb328-c48e-4393-a32d-01dfe691f802','Món này giá bao nhiêu thế?','2022-06-22 13:45:11'),('dda4c635-f1ec-11ec-8797-50ebf6963744','8eb540df-0fc6-42d5-bf30-12eb8bda5f24','helloooooo','2022-06-22 12:33:37'),('e1d3d06f-f1ec-11ec-ae91-50ebf6963744','8eb540df-0fc6-42d5-bf30-12eb8bda5f24','commm','2022-06-22 12:33:44'),('eef3d42b-f1ed-11ec-80d1-50ebf6963744','8eb540df-0fc6-42d5-bf30-12eb8bda5f24','HAHA','2022-06-22 12:41:16');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-22 20:48:45
