-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: employee_management
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `employee_info`
--

DROP TABLE IF EXISTS `employee_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_info` (
  `ID` char(6) NOT NULL,
  `Name` varchar(40) NOT NULL,
  `Gender` char(1) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  `Level_of_Access` char(1) DEFAULT NULL,
  `Salary` int DEFAULT NULL,
  `Age` int DEFAULT NULL,
  `Date_Of_Joining` date DEFAULT NULL,
  `Password` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_info`
--

LOCK TABLES `employee_info` WRITE;
/*!40000 ALTER TABLE `employee_info` DISABLE KEYS */;
INSERT INTO `employee_info` VALUES ('542488','Chelsea Greene','F','HR','1',2000000,25,'2010-05-06','chelseavoyager3'),('546942','Katherine Fernandez','F','HR','1',2400000,47,'2005-08-14','Katherinelovescats22'),('546947','Alan Mason','M','HR','1',2400000,35,'2009-03-11','StonedHarmony'),('546981','Thomas Riley','M','Analytics','2',5200000,47,'2005-08-14','Thomas_Riley1234'),('563223','Dennis Sharp','M','Analytics','1',1800000,25,'2017-08-22','Dionysius_Sharp9999');
/*!40000 ALTER TABLE `employee_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-07  2:24:08