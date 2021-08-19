CREATE DATABASE  IF NOT EXISTS `covidcard` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `covidcard`;
-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: covidcard
-- ------------------------------------------------------
-- Server version	8.0.18

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
-- Table structure for table `covid_infection`
--

DROP TABLE IF EXISTS `covid_infection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `covid_infection` (
  `cov_id` varchar(45) NOT NULL,
  `hospital` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `date` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`cov_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `covid_infection`
--

LOCK TABLES `covid_infection` WRITE;
/*!40000 ALTER TABLE `covid_infection` DISABLE KEYS */;
INSERT INTO `covid_infection` VALUES ('1','Apollo','Infected','10/3/2020'),('10','MGM','Infected','20/11/2020'),('11','','Not Infected',''),('12','','Not Infected',''),('13','','Not Infected',''),('2','MGM','Infected','11/5/2020'),('3','','Not Infected',''),('4','Apollo','Infected','15/5/2021'),('5','Apollo','Infected','15/10/2020'),('6','Apollo','Infected','22/12/2020'),('7','','Not Infected',''),('8','','Not Infected',''),('9','DY','Infected','05/1/2021');
/*!40000 ALTER TABLE `covid_infection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `covid_vaccine`
--

DROP TABLE IF EXISTS `covid_vaccine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `covid_vaccine` (
  `cov_id` varchar(45) NOT NULL,
  `vaccine_name` varchar(45) DEFAULT NULL,
  `centre1` varchar(45) DEFAULT NULL,
  `status1` varchar(45) DEFAULT NULL,
  `date1` varchar(45) DEFAULT NULL,
  `centre2` varchar(45) DEFAULT NULL,
  `status2` varchar(45) DEFAULT NULL,
  `date2` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`cov_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `covid_vaccine`
--

LOCK TABLES `covid_vaccine` WRITE;
/*!40000 ALTER TABLE `covid_vaccine` DISABLE KEYS */;
INSERT INTO `covid_vaccine` VALUES ('1','Covaxine','kollam','Vaccinated','5/3/2021','kollam','Vaccinated','5/4/2021'),('10','Covishield','Malappuram','Vaccinated','12/04/2021','Malappuram','Vaccinated','25/04/2021'),('11','Covaxine','Kasaragod','Vaccinated','2/05/2021','Kasaragod','Vaccinated','5/06/2021'),('12','','','Not Vaccinated','','','Not Vaccinated',''),('13','','','Not Vaccinated','','','Not Vaccinated',''),('2','Covishield','Alappuzha','Vaccinated','15/4/2021','Alappuzha','Vaccinated','19/5/2021'),('3','Covishield','Varkal','Vaccinated','15/5/2021','','Not Vaccinated',''),('4','','','Not Vaccinated','','','Not Vaccinated',''),('5','Covaxine','Ernakulam','Vaccinated','11/4/2021','Ernakulam','Vaccinated','01/6/2021'),('6','Covishield','Thrissur','Vaccinated','8/6/2021','','Not Vaccinated',''),('7','','','Not Vaccinated','','','Not Vaccinated',''),('8','','','Not Vaccinated','','','Not Vaccinated',''),('9','Covaxine','Wayanadu','Vaccinated','25/05/2021','','Not Vaccinated','');
/*!40000 ALTER TABLE `covid_vaccine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor` (
  `Doc_ID` varchar(45) DEFAULT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Cov_ID` varchar(45) NOT NULL,
  PRIMARY KEY (`Cov_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES ('100','Dr.Ram','1'),('650','Dr.Kohli','10'),('750','Dr.Ambar','11'),('759','Dr.Prakhar','12'),('1000','Dr.Prakash','13'),('200','Dr.Ben','2'),('250','Dr.Sharma','3'),('350','Dr.Mohit','4'),('50','Dr.Aparna','5'),('10','Dr.Khatri','6'),('125','Dr.BalaKrishnan','7'),('500','Dr.Anika','8'),('550','Dr.Bakshi','9');
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient` (
  `cov_id` varchar(45) NOT NULL,
  `firstname` varchar(45) DEFAULT NULL,
  `surname` varchar(45) DEFAULT NULL,
  `aadhar_no` varchar(45) DEFAULT NULL,
  `District` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`cov_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES ('1','Rahul','Garg','50023','Kollam'),('10','Ishaan','Yadav','203925','Malappuram'),('11','Aditi','Arya','53925','Kasaragod'),('12','Nikhil','Varma','18925','Kozhikode'),('13','Rajesh','Verma','198925','Kollam'),('2','Raj','Sharma','90045','Alappuzha'),('3','Sham','Khanna','92345','Thiruvananthapuram'),('4','Sahil','Sayani','85432','Idukki'),('5','Medha','Patel','27432','Ernakulam'),('6','Karan','Agrawal','67875','Thrissur'),('7','Anushka','Sharma','72815','Palakkad'),('8','Mannit','Parik','102815','Kannur'),('9','Ananya','Reddy','103925','Wayanadu');
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-18 23:43:24
