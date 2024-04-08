-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mar. 09 avr. 2024 à 01:25
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `liste_objet`
--

-- --------------------------------------------------------

--
-- Structure de la table `fileattente`
--

CREATE TABLE `fileattente` (
  `id` int(11) NOT NULL,
  `nom` varchar(40) NOT NULL,
  `prioritaire` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `fileattente`
--

INSERT INTO `fileattente` (`id`, `nom`, `prioritaire`) VALUES
(2, 'Alice', 0),
(3, 'bob', 0),
(6, 'Robert', 0),
(7, 'Luc', 0),
(8, 'Ginette', 1),
(9, 'Jason', 0),
(10, 'Rober', 1);

-- --------------------------------------------------------

--
-- Structure de la table `personnes`
--

CREATE TABLE `personnes` (
  `nom` varchar(30) NOT NULL,
  `age` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `personnes`
--

INSERT INTO `personnes` (`nom`, `age`) VALUES
('Ginette', 64),
('Bob', 52),
('John', 32),
('Alice', 23),
('Rambo', 60),
('Marie', 56),
('Genevieve', 34),
('roger', 65),
('luc', 56);

-- --------------------------------------------------------

--
-- Structure de la table `reservation`
--

CREATE TABLE `reservation` (
  `nom` varchar(30) NOT NULL,
  `place` int(50) NOT NULL,
  `place_speciale` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `reservation`
--

INSERT INTO `reservation` (`nom`, `place`, `place_speciale`) VALUES
('Alice', 5, 0),
('John', 0, 1),
('jesus', 12, 0),
('dude', 0, 2);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `fileattente`
--
ALTER TABLE `fileattente`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `fileattente`
--
ALTER TABLE `fileattente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
