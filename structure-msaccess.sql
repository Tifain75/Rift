
-- Power_Armor definition
 

CREATE TABLE Power_Armor (
	Id_Power_Armor INTEGER  PRIMARY KEY NOT NULL,
	VehicleName VARCHAR(69) UNIQUE KEY NOT NULL,
	Description TEXT,
	Model TEXT,
	Class TEXT,
	Crew TEXT,
	Notes TEXT,
	GroundSpeed TEXT,
	FlySpeed TEXT,
	Flyrange TEXT,
	Height TEXT,
	Width TEXT,
	Length TEXT,
	Weight TEXT,
	Cargo TEXT,
	PowerSystem TEXT,
	Classification VARCHAR(255),
	BlackMarketCost TEXT,
	PAL VARCHAR(1)

);

SELECT `VehicleName`, `Description`, `Model`, `Class`, `Crew`, `Notes`, `GroundSpeed`, `FlySpeed`, `Flyrange`, `Height`,
 `Width`, `Length`, `Weight`, `Cargo`, `PowerSystem`, `Classification`, `BlackMarketCost`, PAL, `Page`
FROM `Power_Armor`;

 
-- Power_Armor_MDC definition
 

CREATE TABLE Power_Armor_MDC (
	Id_PA_MCD INTEGER  PRIMARY KEY NOT NULL,
	Location VARCHAR(69),
	MDC SMALLINT ,
	Id_Power_Armor INTEGER  FOREIGN KEY (Id_Power_Armor) REFERENCES Power_Armor (Id_Power_Armor) ON DELETE CASCADE ON UPDATE CASCADE
);

SELECT `VehicleName`, `Location`, MDC
FROM `Power_Armor_MDC`;


-- Power_Armor_Weapons definition


CREATE TABLE Power_Armor_Weapons (
	Id_PA_Weapons INTEGER  PRIMARY KEY NOT NULL,
	Weapon TEXT,
	Description TEXT,
	PrimaryPurpose TEXT,
	SecondaryPurpose TEXT,
	MissileType TEXT,
	MegaDamage TEXT,
	Range TEXT,
	RateofFir TEXT,
	Payload TEXT,
	Id_Power_Armor INTEGER  FOREIGN KEY (Id_Power_Armor) REFERENCES Power_Armor (Id_Power_Armor) ON DELETE CASCADE ON UPDATE CASCADE
);

SELECT `VehicleName`, `Weapon`, `Description`, `PrimaryPurpose`, `SecondaryPurpose`, `MissileType`, `MegaDamage`, `Range`, `RateofFir`, `Payload`
FROM `Power_Armor_Weapons`;
