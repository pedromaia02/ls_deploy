CREATE DATABASE  IF NOT EXISTS `ls` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `ls`;
-- MySQL dump 10.13  Distrib 5.5.52, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: ls
-- ------------------------------------------------------
-- Server version	5.5.52-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `legendas`
--

DROP TABLE IF EXISTS `legendas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `legendas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `legendas`
--

LOCK TABLES `legendas` WRITE;
/*!40000 ALTER TABLE `legendas` DISABLE KEYS */;
INSERT INTO `legendas` VALUES (1,'MATERIAIS DE OBRA'),(2,'COMBUSTIVEL'),(3,'DESPESAS OPERACIONAIS'),(4,'FOLHA DE PAGAMENTO'),(5,'MANUTENCAO VEICULOS'),(6,'UNIFORMES, FERAMENTAS, EPI'),(7,'MATERIAIS CONSUMO'),(8,'DESPESAS VIAGEM');
/*!40000 ALTER TABLE `legendas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `contrato` varchar(45) DEFAULT NULL,
  `data` date DEFAULT NULL,
  `legenda` varchar(45) DEFAULT NULL,
  `valor` float DEFAULT NULL,
  `tipo` varchar(45) DEFAULT NULL,
  `detalhe` varchar(500) DEFAULT NULL,
  `anexo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES (5,'PETROLINA','2016-09-07','MATERIAIS CONSUMO',222,'SAIDA','aaaaa','documents/2016/09/07/Firefox_wallpaper.png'),(19,'TRT','2016-09-07','DESPESAS VIAGEM',502.02,'ENTRADA','saaa',''),(20,'TRT','2016-10-10','MANUTENCAO VEICULOS',600,'SAIDA','scvsdfv',''),(21,'FORTALEZA','2016-09-07','COMBUSTIVEL',500,'ENTRADA','eqrfwgef','documents/2016/09/08/examples.desktop'),(22,'JUAZEIRO','2016-09-11','MATERIAIS DE OBRA',100,'SAIDA','afdsgvfdb',''),(23,'BAHIA','2016-09-11','DESPESAS OPERACIONAIS',90,'SAIDA','aewgesrbs','documents/2016/09/12/FINANCEIRO_2016_Salvo_automaticamente.xls'),(24,'BAHIA','2016-09-12','MATERIAIS DE OBRA',500,'ENTRADA','asfesgfsg',''),(25,'PETROLINA','2016-09-12','UNIFORMES, FERAMENTAS, EPI',500,'ENTRADA','sdvfbgf',''),(26,'JUAZEIRO','2016-09-12','FOLHA DE PAGAMENTO',500,'ENTRADA','dfhjhty',''),(28,'TRT','2016-09-12','FOLHA DE PAGAMENTO',200,'SAIDA','svdsadcsad',''),(29,'TRT','2016-09-12','DESPESAS OPERACIONAIS',300,'SAIDA','WFEWQFQ',''),(30,'TRT','2016-09-12','MATERIAIS DE OBRA',22,'SAIDA','wfvewfg','documents/2016/09/12/FOLHA.pdf');
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contratos`
--

DROP TABLE IF EXISTS `contratos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contratos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contratos`
--

LOCK TABLES `contratos` WRITE;
/*!40000 ALTER TABLE `contratos` DISABLE KEYS */;
INSERT INTO `contratos` VALUES (1,'TRT'),(2,'FORTALEZA'),(3,'SOBRAL'),(4,'JUAZEIRO'),(5,'INSS-NATAL'),(6,'PETROLINA'),(7,'IMPERATRIZ');
/*!40000 ALTER TABLE `contratos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-10-02 10:23:51
