SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

DROP SCHEMA IF EXISTS `grcp_bd` ;
CREATE SCHEMA IF NOT EXISTS `grcp_bd` DEFAULT CHARACTER SET utf8 ;
USE `grcp_bd` ;

-- -----------------------------------------------------
-- Table `grcp_bd`.`tipo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `grcp_bd`.`tipo` ;

CREATE  TABLE IF NOT EXISTS `grcp_bd`.`tipo` (
  `idTipo` INT(11) NOT NULL AUTO_INCREMENT ,
  `tipo_medicamento` VARCHAR(45) NOT NULL ,
  `activo` TINYINT(1) NOT NULL ,
  PRIMARY KEY (`idTipo`) )
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `grcp_bd`.`medicamento`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `grcp_bd`.`medicamento` ;

CREATE  TABLE IF NOT EXISTS `grcp_bd`.`medicamento` (
  `idMedicamento` INT(11) NOT NULL AUTO_INCREMENT ,
  `nombre_comercial` VARCHAR(100) NOT NULL ,
  `codigo` VARCHAR(12) NOT NULL ,
  `droga` VARCHAR(100) NOT NULL ,
  `Tipo_idTipo` INT(11) NOT NULL ,
  PRIMARY KEY (`idMedicamento`, `Tipo_idTipo`) ,
  INDEX `fk_Medicamento_Tipo_idx` (`Tipo_idTipo` ASC) ,
  CONSTRAINT `fk_Medicamento_Tipo`
    FOREIGN KEY (`Tipo_idTipo` )
    REFERENCES `grcp_bd`.`tipo` (`idTipo` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8;

USE `grcp_bd` ;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
