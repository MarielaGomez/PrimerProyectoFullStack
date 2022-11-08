-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 10-03-2021 a las 22:42:56
-- Versión del servidor: 5.7.31
-- Versión de PHP: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `app_citas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sexo_interes`
--

DROP TABLE IF EXISTS `level`;
CREATE TABLE IF NOT EXISTS `level` (
  `id_lev` int(3) NOT NULL,
  `nom_lev` varchar(20) NOT NULL,
  PRIMARY KEY (`id_lev`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `sexo_interes`
--

INSERT INTO `level` (`id_lev`, `nom_lev`) VALUES
(1, 'Nivel 1'),
(2, 'Nivel 2'),
(3, 'Nivel 3');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tip_usu`
--

DROP TABLE IF EXISTS `tip_usu`;
CREATE TABLE IF NOT EXISTS `tip_usu` (
  `id_tip_usu` int(11) NOT NULL,
  `nom_tip_usu` varchar(20) NOT NULL,
  PRIMARY KEY (`id_tip_usu`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tip_usu`
--

INSERT INTO `tip_usu` (`id_tip_usu`, `nom_tip_usu`) VALUES
(1, 'Admin'),
(2, 'Estandar'),
(3, 'Premium');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `fullname` varchar(20) NOT NULL,
  `dni` int(10) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(102) NOT NULL,
  `nombres` varchar(20) NOT NULL,
  `apellido` varchar(20) NOT NULL,
  `direccion` varchar(20) NOT NULL,
  `numeracion` int(10) NOT NULL,
  `id_lev_usu` varchar(11) NOT NULL,
  `tipo` varchar(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_lev_usu` (`id_lev_usu`),
  KEY `tipo` (`tipo`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
