-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema wines
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema wines
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `wines` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `wines` ;

-- -----------------------------------------------------
-- Table `wines`.`data`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `wines`.`data` (
  `index` BIGINT NULL DEFAULT NULL,
  `winery` TEXT NULL DEFAULT NULL,
  `wine` TEXT NULL DEFAULT NULL,
  `year` TEXT NULL DEFAULT NULL,
  `rating` DOUBLE NULL DEFAULT NULL,
  `num_reviews` BIGINT NULL DEFAULT NULL,
  `region` TEXT NULL DEFAULT NULL,
  `price` DOUBLE NULL DEFAULT NULL,
  `type` TEXT NULL DEFAULT NULL,
  `body` DOUBLE NULL DEFAULT NULL,
  `acidity` DOUBLE NULL DEFAULT NULL,
  `parker_score` TEXT NULL DEFAULT NULL,
  INDEX `ix_data_index` (`index` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
