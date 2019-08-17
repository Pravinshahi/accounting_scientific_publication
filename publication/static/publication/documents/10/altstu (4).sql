-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 15, 2019 at 07:30 AM
-- Server version: 10.3.15-MariaDB
-- PHP Version: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `altstu`
--

-- --------------------------------------------------------

--
-- Table structure for table `academic_degree`
--

CREATE TABLE `academic_degree` (
  `ID_academic_degree` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `academic_degree`
--

INSERT INTO `academic_degree` (`ID_academic_degree`, `Name`) VALUES
(1, 'Кандидат наук'),
(2, 'Доктор наук');

-- --------------------------------------------------------

--
-- Table structure for table `academic_title`
--

CREATE TABLE `academic_title` (
  `ID_academic_title` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `academic_title`
--

INSERT INTO `academic_title` (`ID_academic_title`, `Name`) VALUES
(1, 'Доцент'),
(2, 'Профессор');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add department', 7, 'add_department'),
(26, 'Can change department', 7, 'change_department'),
(27, 'Can delete department', 7, 'delete_department'),
(28, 'Can view department', 7, 'view_department'),
(29, 'Can add type_publication', 8, 'add_type_publication'),
(30, 'Can change type_publication', 8, 'change_type_publication'),
(31, 'Can delete type_publication', 8, 'delete_type_publication'),
(32, 'Can view type_publication', 8, 'view_type_publication'),
(33, 'Can add status', 9, 'add_status'),
(34, 'Can change status', 9, 'change_status'),
(35, 'Can delete status', 9, 'delete_status'),
(36, 'Can view status', 9, 'view_status'),
(37, 'Can add bibliographic_database', 10, 'add_bibliographic_database'),
(38, 'Can change bibliographic_database', 10, 'change_bibliographic_database'),
(39, 'Can delete bibliographic_database', 10, 'delete_bibliographic_database'),
(40, 'Can view bibliographic_database', 10, 'view_bibliographic_database'),
(41, 'Can add publication employee', 11, 'add_publicationemployee'),
(42, 'Can change publication employee', 11, 'change_publicationemployee'),
(43, 'Can delete publication employee', 11, 'delete_publicationemployee'),
(44, 'Can view publication employee', 11, 'view_publicationemployee'),
(45, 'Can add publication', 12, 'add_publication'),
(46, 'Can change publication', 12, 'change_publication'),
(47, 'Can delete publication', 12, 'delete_publication'),
(48, 'Can view publication', 12, 'view_publication'),
(49, 'Can add faculty', 13, 'add_faculty'),
(50, 'Can change faculty', 13, 'change_faculty'),
(51, 'Can delete faculty', 13, 'delete_faculty'),
(52, 'Can view faculty', 13, 'view_faculty'),
(53, 'Can add employee', 14, 'add_employee'),
(54, 'Can change employee', 14, 'change_employee'),
(55, 'Can delete employee', 14, 'delete_employee'),
(56, 'Can view employee', 14, 'view_employee'),
(57, 'Can add publication bibliographic_database', 15, 'add_publicationbibliographic_database'),
(58, 'Can change publication bibliographic_database', 15, 'change_publicationbibliographic_database'),
(59, 'Can delete publication bibliographic_database', 15, 'delete_publicationbibliographic_database'),
(60, 'Can view publication bibliographic_database', 15, 'view_publicationbibliographic_database'),
(61, 'Can add magazine', 16, 'add_magazine'),
(62, 'Can change magazine', 16, 'change_magazine'),
(63, 'Can delete magazine', 16, 'delete_magazine'),
(64, 'Can view magazine', 16, 'view_magazine'),
(65, 'Can add year', 17, 'add_year'),
(66, 'Can change year', 17, 'change_year'),
(67, 'Can delete year', 17, 'delete_year'),
(68, 'Can view year', 17, 'view_year'),
(69, 'Can add academic_title', 18, 'add_academic_title'),
(70, 'Can change academic_title', 18, 'change_academic_title'),
(71, 'Can delete academic_title', 18, 'delete_academic_title'),
(72, 'Can view academic_title', 18, 'view_academic_title'),
(73, 'Can add city', 19, 'add_city'),
(74, 'Can change city', 19, 'change_city'),
(75, 'Can delete city', 19, 'delete_city'),
(76, 'Can view city', 19, 'view_city'),
(77, 'Can add academic_degree', 20, 'add_academic_degree'),
(78, 'Can change academic_degree', 20, 'change_academic_degree'),
(79, 'Can delete academic_degree', 20, 'delete_academic_degree'),
(80, 'Can view academic_degree', 20, 'view_academic_degree'),
(81, 'Can add position', 21, 'add_position'),
(82, 'Can change position', 21, 'change_position'),
(83, 'Can delete position', 21, 'delete_position'),
(84, 'Can view position', 21, 'view_position'),
(85, 'Can add publisher', 22, 'add_publisher'),
(86, 'Can change publisher', 22, 'change_publisher'),
(87, 'Can delete publisher', 22, 'delete_publisher'),
(88, 'Can view publisher', 22, 'view_publisher'),
(89, 'Can add benefit_type', 23, 'add_benefit_type'),
(90, 'Can change benefit_type', 23, 'change_benefit_type'),
(91, 'Can delete benefit_type', 23, 'delete_benefit_type'),
(92, 'Can view benefit_type', 23, 'view_benefit_type'),
(93, 'Can add vulture', 24, 'add_vulture'),
(94, 'Can change vulture', 24, 'change_vulture'),
(95, 'Can delete vulture', 24, 'delete_vulture'),
(96, 'Can view vulture', 24, 'view_vulture'),
(97, 'Can add type_article', 25, 'add_type_article'),
(98, 'Can change type_article', 25, 'change_type_article'),
(99, 'Can delete type_article', 25, 'delete_type_article'),
(100, 'Can view type_article', 25, 'view_type_article');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `benefit_type`
--

CREATE TABLE `benefit_type` (
  `ID_benefit_type` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `benefit_type`
--

INSERT INTO `benefit_type` (`ID_benefit_type`, `Name`) VALUES
(1, 'Учебник'),
(2, 'Учебное пособие'),
(3, 'Учебно-методическое пособие'),
(4, 'Отсутствует');

-- --------------------------------------------------------

--
-- Table structure for table `bibliographic_database`
--

CREATE TABLE `bibliographic_database` (
  `ID_bibliographic_database` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bibliographic_database`
--

INSERT INTO `bibliographic_database` (`ID_bibliographic_database`, `Name`) VALUES
(1, 'Web Of Science'),
(2, 'RISC'),
(3, 'BAK'),
(4, 'ERIH'),
(5, 'Scopus'),
(6, 'Google scholar'),
(7, '13');

-- --------------------------------------------------------

--
-- Table structure for table `city`
--

CREATE TABLE `city` (
  `ID_city` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Confirmed` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `city`
--

INSERT INTO `city` (`ID_city`, `Name`, `Confirmed`) VALUES
(1, 'Барнаул', 1),
(2, 'Новосибирск', 1),
(3, 'Отсутствует', 1);

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `ID_department` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `ID_faculty_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`ID_department`, `Name`, `ID_faculty_id`) VALUES
(1, 'Прикладная математика', 2),
(2, 'Информационные технологии', 2),
(3, 'Информационные системы в экономике', 2),
(4, 'Информатики, вычислительной техники и информационной безопасности', 2),
(5, 'Высшая математика', 2),
(6, 'Высшая математика  и математическое моделирование', 2),
(7, 'Кафедра электротехники и автоматизированного электропривода ', 5),
(8, 'Кафедра электрификации производства и быта', 5),
(9, 'Кафедра электроснабжения промышленных предприятий', 2),
(10, 'Кафедра государственной налоговой службы', 9),
(11, 'Кафедра международных экономических отношений', 9),
(12, 'Кафедра экономики, финансов и кредита ', 9),
(13, 'Кафедра менеджмента', 9),
(14, 'Кафедра экономики и производственного менеджмента', 9),
(15, 'Кафедра экономической теории и предпринимательства', 9),
(16, 'jk', 6);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(20, 'publication', 'academic_degree'),
(18, 'publication', 'academic_title'),
(23, 'publication', 'benefit_type'),
(10, 'publication', 'bibliographic_database'),
(19, 'publication', 'city'),
(7, 'publication', 'department'),
(14, 'publication', 'employee'),
(13, 'publication', 'faculty'),
(16, 'publication', 'magazine'),
(21, 'publication', 'position'),
(12, 'publication', 'publication'),
(15, 'publication', 'publicationbibliographic_database'),
(11, 'publication', 'publicationemployee'),
(22, 'publication', 'publisher'),
(9, 'publication', 'status'),
(25, 'publication', 'type_article'),
(8, 'publication', 'type_publication'),
(24, 'publication', 'vulture'),
(17, 'publication', 'year'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-06-09 09:06:43.273622'),
(2, 'auth', '0001_initial', '2019-06-09 09:06:43.429879'),
(3, 'admin', '0001_initial', '2019-06-09 09:06:43.820496'),
(4, 'admin', '0002_logentry_remove_auto_add', '2019-06-09 09:06:44.008002'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2019-06-09 09:06:44.008002'),
(6, 'contenttypes', '0002_remove_content_type_name', '2019-06-09 09:06:44.164248'),
(7, 'auth', '0002_alter_permission_name_max_length', '2019-06-09 09:06:44.242372'),
(8, 'auth', '0003_alter_user_email_max_length', '2019-06-09 09:06:44.320508'),
(9, 'auth', '0004_alter_user_username_opts', '2019-06-09 09:06:44.320508'),
(10, 'auth', '0005_alter_user_last_login_null', '2019-06-09 09:06:44.398620'),
(11, 'auth', '0006_require_contenttypes_0002', '2019-06-09 09:06:44.398620'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2019-06-09 09:06:44.414251'),
(13, 'auth', '0008_alter_user_username_max_length', '2019-06-09 09:06:44.570497'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2019-06-09 09:06:44.632998'),
(15, 'auth', '0010_alter_group_name_max_length', '2019-06-09 09:06:44.695500'),
(16, 'auth', '0011_update_proxy_permissions', '2019-06-09 09:06:44.711125'),
(17, 'sessions', '0001_initial', '2019-06-09 09:06:44.757997'),
(18, 'publication', '0001_initial', '2019-06-09 09:14:04.985574'),
(19, 'publication', '0002_publication_file', '2019-06-13 05:20:52.009590'),
(20, 'publication', '0003_publisher', '2019-06-14 02:48:13.248656'),
(21, 'publication', '0004_publication_id_publisher', '2019-06-14 02:56:55.415452'),
(22, 'publication', '0005_remove_publication_id_publisher', '2019-06-14 03:00:47.749266'),
(23, 'publication', '0006_publication_id_publisher', '2019-06-14 03:01:47.827351'),
(24, 'publication', '0007_benefit_type', '2019-06-14 12:17:11.801089'),
(25, 'publication', '0008_publication_id_benefit_type', '2019-06-14 12:22:50.760436'),
(26, 'publication', '0009_vulture', '2019-06-14 12:32:18.401058'),
(27, 'publication', '0010_publication_id_vulture', '2019-06-14 12:36:14.870607'),
(28, 'publication', '0011_type_article', '2019-06-14 14:28:40.013693'),
(29, 'publication', '0012_publication_id_type_article', '2019-06-15 02:18:46.796542');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `ID_employee` int(11) NOT NULL,
  `login` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `FIO` varchar(255) NOT NULL,
  `Date` date NOT NULL,
  `ID_academic_degree_id` int(11) NOT NULL,
  `ID_academic_title_id` int(11) NOT NULL,
  `ID_department_id` int(11) NOT NULL,
  `ID_position_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`ID_employee`, `login`, `password`, `FIO`, `Date`, `ID_academic_degree_id`, `ID_academic_title_id`, `ID_department_id`, `ID_position_id`) VALUES
(2, '4', '4', 'Елисеев Петр Витальевич', '1978-05-14', 1, 1, 8, 1),
(3, '2', '2', 'Рыбаков Михаил Антонинович', '1968-02-14', 2, 2, 14, 1),
(4, '3', '3', 'Соболев Ярослав Кириллович', '1981-07-12', 1, 1, 13, 1),
(5, 'sfda', '32', 'sdf1', '2019-06-20', 2, 2, 15, 3);

-- --------------------------------------------------------

--
-- Table structure for table `faculty`
--

CREATE TABLE `faculty` (
  `ID_faculty` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `faculty`
--

INSERT INTO `faculty` (`ID_faculty`, `Name`) VALUES
(1, 'Гуманитарный факультет'),
(2, 'Факультет информационных технологий'),
(3, 'Факультет специальных технологий'),
(4, 'Строительно-технологический факультет'),
(5, 'Энергетический факультет'),
(6, 'Факультет энергомашиностроения и автомобильного транспорта'),
(7, 'Институт архитектуры и дизайна '),
(8, 'Институт биотехнологии, пищевой и химической инженерии'),
(9, 'Институт экономики и управления '),
(10, '12'),
(11, '212');

-- --------------------------------------------------------

--
-- Table structure for table `magazine`
--

CREATE TABLE `magazine` (
  `ID_magazine` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Confirmed` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `magazine`
--

INSERT INTO `magazine` (`ID_magazine`, `Name`, `Confirmed`) VALUES
(1, 'Academy of Strategic Management Journal', 0),
(2, 'NovaInfo', 0),
(3, 'Nanoscale', 0),
(4, 'INFORMATION INNOVATE TECHNOLOGIES', 0),
(5, 'Surface Science', 0),
(6, 'Известия Ран', 0),
(7, 'Компьютерное исследование и моделирование', 0),
(8, 'Интеграция наук', 0),
(9, 'Ползуновский вестник', 0),
(10, 'Научное обозрение', 0),
(11, 'Отсутствует', 1);

-- --------------------------------------------------------

--
-- Table structure for table `position`
--

CREATE TABLE `position` (
  `ID_position` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `position`
--

INSERT INTO `position` (`ID_position`, `Name`) VALUES
(1, 'Преподаватель'),
(2, 'Заведующий кафедры'),
(3, 'Декан');

-- --------------------------------------------------------

--
-- Table structure for table `publication`
--

CREATE TABLE `publication` (
  `ID_publication` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Date` date NOT NULL,
  `Note` varchar(255) NOT NULL,
  `Link` varchar(255) NOT NULL,
  `Initial_page` varchar(255) NOT NULL,
  `Page_final` varchar(255) NOT NULL,
  `Tom` varchar(255) NOT NULL,
  `Issue_number` varchar(255) NOT NULL,
  `DOI` varchar(255) NOT NULL,
  `ISBN` varchar(255) NOT NULL,
  `ID_city_id` int(11) NOT NULL,
  `ID_employee_id` int(11) NOT NULL,
  `ID_magazine_id` int(11) NOT NULL,
  `ID_status_id` int(11) NOT NULL,
  `ID_type_publication_id` int(11) NOT NULL,
  `ID_year_id` int(11) NOT NULL,
  `File` varchar(255) NOT NULL,
  `ID_publisher_id` int(11) NOT NULL,
  `ID_benefit_type_id` int(11) NOT NULL,
  `ID_vulture_id` int(11) NOT NULL,
  `ID_type_article_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `publication`
--

INSERT INTO `publication` (`ID_publication`, `Name`, `Date`, `Note`, `Link`, `Initial_page`, `Page_final`, `Tom`, `Issue_number`, `DOI`, `ISBN`, `ID_city_id`, `ID_employee_id`, `ID_magazine_id`, `ID_status_id`, `ID_type_publication_id`, `ID_year_id`, `File`, `ID_publisher_id`, `ID_benefit_type_id`, `ID_vulture_id`, `ID_type_article_id`) VALUES
(2, 'ПРОСТРАНСТВЕННЫЕ ОГРАНИЧЕНИЯ ПОЛИТИКИ ЦЕНОВОЙ СТАБИЛЬНОСТИ В РОССИЙСКОЙ ФЕДЕРАЦИИ', '2019-05-08', 'Статья посвящена оценке пространственных ограничений политики ценовой стабильности в России.', 'https://cyberleninka.ru/article/n/prostranstvennye-ogranicheniya-politiki-tsenovoy-stabilnosti-v-rossiyskoy-federatsii', '', '', '', '', '3123212213', '423432432432423', 1, 3, 1, 1, 3, 2, ' ', 1, 4, 5, 3),
(3, 'w', '2019-06-13', '', '', '', '', '', '342', '324', '234', 1, 2, 8, 3, 1, 2, ' ', 1, 4, 5, 3),
(5, 'sdf', '2019-06-13', '', '', '', '', '', '2', '432', '2', 2, 2, 11, 3, 1, 3, ' ', 1, 4, 5, 3),
(6, 'dfs', '2019-06-13', '', '', '', '', '', 'dfs', 'dsf', 'sdf', 2, 2, 8, 3, 1, 2, ' ', 1, 4, 5, 3),
(7, 'jkl', '2019-06-13', '', '', '', '', '', 'j', 'jk', 'j', 2, 2, 11, 3, 1, 3, '33ca0d707a0867ad39d253b4b98fb177.jpg', 4, 4, 5, 3),
(9, '2345', '2019-06-14', '24', '234', '', '', '', '2', '234', '324', 2, 2, 11, 3, 1, 3, 'altstu.sql', 5, 4, 5, 3),
(10, 'df', '2019-06-15', '234', '23', '3', '4', '3', '2', '234', '', 3, 2, 4, 3, 3, 2, 'altstu.sql', 5, 4, 5, 2);

-- --------------------------------------------------------

--
-- Table structure for table `publication_bibliographic`
--

CREATE TABLE `publication_bibliographic` (
  `ID_publication_bibliographic` int(11) NOT NULL,
  `ID_bibliographic_database_id` int(11) NOT NULL,
  `ID_publication_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `publication_employee`
--

CREATE TABLE `publication_employee` (
  `ID_publication_employee` int(11) NOT NULL,
  `ID_employee_id` int(11) NOT NULL,
  `ID_publication_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `publisher`
--

CREATE TABLE `publisher` (
  `ID_publisher` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Confirmed` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `publisher`
--

INSERT INTO `publisher` (`ID_publisher`, `Name`, `Confirmed`) VALUES
(1, 'Алтайский государственный технический университет им. И.И.Ползунова', 1),
(2, 'Новосибирский государственный технический университет', 1),
(4, 'Наука и образование', 1),
(5, 'Издательство научно-технической литературы(Томск)', 1);

-- --------------------------------------------------------

--
-- Table structure for table `status`
--

CREATE TABLE `status` (
  `ID_status` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `status`
--

INSERT INTO `status` (`ID_status`, `Name`) VALUES
(1, 'Опубликовано'),
(2, 'Отклонено'),
(3, 'Ожидает подтверждения');

-- --------------------------------------------------------

--
-- Table structure for table `type_article`
--

CREATE TABLE `type_article` (
  `ID_type_article` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `type_article`
--

INSERT INTO `type_article` (`ID_type_article`, `Name`) VALUES
(1, 'Научная статья'),
(2, 'Научно-популярная статья'),
(3, 'Отсутствует');

-- --------------------------------------------------------

--
-- Table structure for table `type_publication`
--

CREATE TABLE `type_publication` (
  `ID_type_publication` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `type_publication`
--

INSERT INTO `type_publication` (`ID_type_publication`, `Name`) VALUES
(1, 'Монография'),
(2, 'Пособие'),
(3, 'Статья'),
(4, 'НИР');

-- --------------------------------------------------------

--
-- Table structure for table `vulture`
--

CREATE TABLE `vulture` (
  `ID_vulture` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `vulture`
--

INSERT INTO `vulture` (`ID_vulture`, `Name`) VALUES
(1, 'Министерство образования'),
(2, 'АлтГТУ'),
(3, 'ФУМО'),
(4, 'Координационный НМЦ'),
(5, 'Отсутствует');

-- --------------------------------------------------------

--
-- Table structure for table `year`
--

CREATE TABLE `year` (
  `ID_year` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `year`
--

INSERT INTO `year` (`ID_year`, `Name`) VALUES
(1, '2017'),
(2, '2018'),
(3, '2019');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `academic_degree`
--
ALTER TABLE `academic_degree`
  ADD PRIMARY KEY (`ID_academic_degree`);

--
-- Indexes for table `academic_title`
--
ALTER TABLE `academic_title`
  ADD PRIMARY KEY (`ID_academic_title`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `benefit_type`
--
ALTER TABLE `benefit_type`
  ADD PRIMARY KEY (`ID_benefit_type`);

--
-- Indexes for table `bibliographic_database`
--
ALTER TABLE `bibliographic_database`
  ADD PRIMARY KEY (`ID_bibliographic_database`);

--
-- Indexes for table `city`
--
ALTER TABLE `city`
  ADD PRIMARY KEY (`ID_city`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`ID_department`),
  ADD KEY `department_ID_faculty_id_422f68a6_fk_faculty_ID_faculty` (`ID_faculty_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`ID_employee`),
  ADD KEY `employee_ID_academic_degree_i_5b72dab1_fk_academic_` (`ID_academic_degree_id`),
  ADD KEY `employee_ID_academic_title_id_2895b81d_fk_academic_` (`ID_academic_title_id`),
  ADD KEY `employee_ID_department_id_29b06b2f_fk_department_ID_department` (`ID_department_id`),
  ADD KEY `employee_ID_position_id_cb3ec34e_fk_position_ID_position` (`ID_position_id`);

--
-- Indexes for table `faculty`
--
ALTER TABLE `faculty`
  ADD PRIMARY KEY (`ID_faculty`);

--
-- Indexes for table `magazine`
--
ALTER TABLE `magazine`
  ADD PRIMARY KEY (`ID_magazine`);

--
-- Indexes for table `position`
--
ALTER TABLE `position`
  ADD PRIMARY KEY (`ID_position`);

--
-- Indexes for table `publication`
--
ALTER TABLE `publication`
  ADD PRIMARY KEY (`ID_publication`),
  ADD KEY `publication_ID_city_id_3ea2cd46_fk_city_ID_city` (`ID_city_id`),
  ADD KEY `publication_ID_employee_id_f170bd26_fk_employee_ID_employee` (`ID_employee_id`),
  ADD KEY `publication_ID_magazine_id_7e7f193d_fk_magazine_ID_magazine` (`ID_magazine_id`),
  ADD KEY `publication_ID_status_id_29a8a271_fk_status_ID_status` (`ID_status_id`),
  ADD KEY `publication_ID_type_publication__424ffa41_fk_type_publ` (`ID_type_publication_id`),
  ADD KEY `publication_ID_year_id_28f62cf5_fk_year_ID_year` (`ID_year_id`),
  ADD KEY `publication_ID_publisher_id_af2efc0d_fk_publisher_ID_publisher` (`ID_publisher_id`),
  ADD KEY `publication_ID_benefit_type_id_2f5daf52_fk_benefit_t` (`ID_benefit_type_id`),
  ADD KEY `publication_ID_vulture_id_72890508_fk_vulture_ID_vulture` (`ID_vulture_id`),
  ADD KEY `publication_ID_type_article_id_406e7d30_fk_type_arti` (`ID_type_article_id`);

--
-- Indexes for table `publication_bibliographic`
--
ALTER TABLE `publication_bibliographic`
  ADD PRIMARY KEY (`ID_publication_bibliographic`),
  ADD KEY `publication_bibliogr_ID_bibliographic_dat_f94c6b1c_fk_bibliogra` (`ID_bibliographic_database_id`),
  ADD KEY `publication_bibliogr_ID_publication_id_03528b27_fk_publicati` (`ID_publication_id`);

--
-- Indexes for table `publication_employee`
--
ALTER TABLE `publication_employee`
  ADD PRIMARY KEY (`ID_publication_employee`),
  ADD KEY `publication_employee_ID_employee_id_7c6c2764_fk_employee_` (`ID_employee_id`),
  ADD KEY `publication_employee_ID_publication_id_c84dac2a_fk_publicati` (`ID_publication_id`);

--
-- Indexes for table `publisher`
--
ALTER TABLE `publisher`
  ADD PRIMARY KEY (`ID_publisher`);

--
-- Indexes for table `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`ID_status`);

--
-- Indexes for table `type_article`
--
ALTER TABLE `type_article`
  ADD PRIMARY KEY (`ID_type_article`);

--
-- Indexes for table `type_publication`
--
ALTER TABLE `type_publication`
  ADD PRIMARY KEY (`ID_type_publication`);

--
-- Indexes for table `vulture`
--
ALTER TABLE `vulture`
  ADD PRIMARY KEY (`ID_vulture`);

--
-- Indexes for table `year`
--
ALTER TABLE `year`
  ADD PRIMARY KEY (`ID_year`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `academic_degree`
--
ALTER TABLE `academic_degree`
  MODIFY `ID_academic_degree` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `academic_title`
--
ALTER TABLE `academic_title`
  MODIFY `ID_academic_title` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `benefit_type`
--
ALTER TABLE `benefit_type`
  MODIFY `ID_benefit_type` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `bibliographic_database`
--
ALTER TABLE `bibliographic_database`
  MODIFY `ID_bibliographic_database` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `city`
--
ALTER TABLE `city`
  MODIFY `ID_city` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `department`
--
ALTER TABLE `department`
  MODIFY `ID_department` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `ID_employee` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `faculty`
--
ALTER TABLE `faculty`
  MODIFY `ID_faculty` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `magazine`
--
ALTER TABLE `magazine`
  MODIFY `ID_magazine` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `position`
--
ALTER TABLE `position`
  MODIFY `ID_position` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `publication`
--
ALTER TABLE `publication`
  MODIFY `ID_publication` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `publication_bibliographic`
--
ALTER TABLE `publication_bibliographic`
  MODIFY `ID_publication_bibliographic` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `publication_employee`
--
ALTER TABLE `publication_employee`
  MODIFY `ID_publication_employee` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `publisher`
--
ALTER TABLE `publisher`
  MODIFY `ID_publisher` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `status`
--
ALTER TABLE `status`
  MODIFY `ID_status` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `type_article`
--
ALTER TABLE `type_article`
  MODIFY `ID_type_article` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `type_publication`
--
ALTER TABLE `type_publication`
  MODIFY `ID_type_publication` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `vulture`
--
ALTER TABLE `vulture`
  MODIFY `ID_vulture` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `year`
--
ALTER TABLE `year`
  MODIFY `ID_year` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `department`
--
ALTER TABLE `department`
  ADD CONSTRAINT `department_ID_faculty_id_422f68a6_fk_faculty_ID_faculty` FOREIGN KEY (`ID_faculty_id`) REFERENCES `faculty` (`ID_faculty`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `employee`
--
ALTER TABLE `employee`
  ADD CONSTRAINT `employee_ID_academic_degree_i_5b72dab1_fk_academic_` FOREIGN KEY (`ID_academic_degree_id`) REFERENCES `academic_degree` (`ID_academic_degree`),
  ADD CONSTRAINT `employee_ID_academic_title_id_2895b81d_fk_academic_` FOREIGN KEY (`ID_academic_title_id`) REFERENCES `academic_title` (`ID_academic_title`),
  ADD CONSTRAINT `employee_ID_department_id_29b06b2f_fk_department_ID_department` FOREIGN KEY (`ID_department_id`) REFERENCES `department` (`ID_department`),
  ADD CONSTRAINT `employee_ID_position_id_cb3ec34e_fk_position_ID_position` FOREIGN KEY (`ID_position_id`) REFERENCES `position` (`ID_position`);

--
-- Constraints for table `publication`
--
ALTER TABLE `publication`
  ADD CONSTRAINT `publication_ID_benefit_type_id_2f5daf52_fk_benefit_t` FOREIGN KEY (`ID_benefit_type_id`) REFERENCES `benefit_type` (`ID_benefit_type`),
  ADD CONSTRAINT `publication_ID_city_id_3ea2cd46_fk_city_ID_city` FOREIGN KEY (`ID_city_id`) REFERENCES `city` (`ID_city`),
  ADD CONSTRAINT `publication_ID_employee_id_f170bd26_fk_employee_ID_employee` FOREIGN KEY (`ID_employee_id`) REFERENCES `employee` (`ID_employee`),
  ADD CONSTRAINT `publication_ID_magazine_id_7e7f193d_fk_magazine_ID_magazine` FOREIGN KEY (`ID_magazine_id`) REFERENCES `magazine` (`ID_magazine`),
  ADD CONSTRAINT `publication_ID_publisher_id_af2efc0d_fk_publisher_ID_publisher` FOREIGN KEY (`ID_publisher_id`) REFERENCES `publisher` (`ID_publisher`),
  ADD CONSTRAINT `publication_ID_status_id_29a8a271_fk_status_ID_status` FOREIGN KEY (`ID_status_id`) REFERENCES `status` (`ID_status`),
  ADD CONSTRAINT `publication_ID_type_article_id_406e7d30_fk_type_arti` FOREIGN KEY (`ID_type_article_id`) REFERENCES `type_article` (`ID_type_article`),
  ADD CONSTRAINT `publication_ID_type_publication__424ffa41_fk_type_publ` FOREIGN KEY (`ID_type_publication_id`) REFERENCES `type_publication` (`ID_type_publication`),
  ADD CONSTRAINT `publication_ID_vulture_id_72890508_fk_vulture_ID_vulture` FOREIGN KEY (`ID_vulture_id`) REFERENCES `vulture` (`ID_vulture`),
  ADD CONSTRAINT `publication_ID_year_id_28f62cf5_fk_year_ID_year` FOREIGN KEY (`ID_year_id`) REFERENCES `year` (`ID_year`);

--
-- Constraints for table `publication_bibliographic`
--
ALTER TABLE `publication_bibliographic`
  ADD CONSTRAINT `publication_bibliogr_ID_bibliographic_dat_f94c6b1c_fk_bibliogra` FOREIGN KEY (`ID_bibliographic_database_id`) REFERENCES `bibliographic_database` (`ID_bibliographic_database`),
  ADD CONSTRAINT `publication_bibliogr_ID_publication_id_03528b27_fk_publicati` FOREIGN KEY (`ID_publication_id`) REFERENCES `publication` (`ID_publication`);

--
-- Constraints for table `publication_employee`
--
ALTER TABLE `publication_employee`
  ADD CONSTRAINT `publication_employee_ID_employee_id_7c6c2764_fk_employee_` FOREIGN KEY (`ID_employee_id`) REFERENCES `employee` (`ID_employee`),
  ADD CONSTRAINT `publication_employee_ID_publication_id_c84dac2a_fk_publicati` FOREIGN KEY (`ID_publication_id`) REFERENCES `publication` (`ID_publication`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
