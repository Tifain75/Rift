# coding: utf-8   
from sqlalchemy import delete, insert , update ,  func ,select
from sqlalchemy import Column, Integer, Text ,  String,  create_engine ,ForeignKey , BLOB , Float ,   BigInteger , Boolean, null
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from django.template.defaultfilters import default
from dataclasses import dataclass 
from pickle import NONE
import pyodbc 
 


Base = declarative_base()    # prérequis 

def init_sqlalchemy_rcg_fr():  # Base sqllite-fr
    global engine_rcg_fr
    global Base_rcg_fr 
    global DBSession_rcg_fr 

    Base_rcg_fr = declarative_base()
    DBSession_rcg_fr = scoped_session(sessionmaker())
    BaseSqllite_fr = './Base/baseGenFRS.db'
    dbname = 'sqlite:///' + BaseSqllite_fr
    engine_rcg_fr = create_engine(dbname, echo=False)
    
    Base.metadata.drop_all(engine_rcg_fr)       # drop des tables
    Base.metadata.create_all(engine_rcg_fr)      # uniquement � la creation installe les tables
    DBSession_rcg_fr.remove()
    DBSession_rcg_fr.configure(bind=engine_rcg_fr, autoflush=False, expire_on_commit=False)

def init_sqlalchemy_rcg_gb():  # Base sqllite-fr
    global engine_rcg_gb
    global Base_rcg_gb 
    global DBSession_rcg_gb 

    Base_rcg_gb = declarative_base()
    DBSession_rcg_gb = scoped_session(sessionmaker())
    BaseSqllite_gb = './Base/baseGengb.db'
    dbname = 'sqlite:///' + BaseSqllite_gb
    engine_rcg_gb = create_engine(dbname, echo=False)
    
    Base.metadata.drop_all(engine_rcg_gb)       # drop des tables
    Base.metadata.create_all(engine_rcg_gb)      # uniquement � la creation installe les tables
    DBSession_rcg_gb.remove()
    DBSession_rcg_gb.configure(bind=engine_rcg_gb, autoflush=False, expire_on_commit=False)
    
# definition de la base msaccess
BaseOrigine = (
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        #r"DBQ=C:\Users\serve-e\eclipse-workspace-python\Rift\Base\Animal\rcg.mdb;")
        r"DBQ=.\Base\rcg.mdb;")

class T_GroupeREF( Base ):
    __tablename__ = 'GroupeREF'
    Id_GroupeREF  = Column(Integer, primary_key=True,  autoincrement=True)
    name = Column(String(255) , unique =True ,index =True )
    typeGroup = Column(String(255))
    Description = Column(Text)  

"""
class T_GroupeCompetence( Base ):
    __tablename__ = 'GroupeCompetence'
    Id_GroupeCompetence  = Column(Integer, primary_key=True,  autoincrement=True)
    Nom = Column(String(255) , unique =True ,index =True )
    Description = Column(Text)  

class T_Grouping_Skills( Base ):
    __tablename__ = 'Grouping_Skills'
    ID_Grouping_Skills = Column(Integer, primary_key=True,  autoincrement=True)
    Grouping_Skills_Name = Column(String(50)) 
    Description = Column(Text)      

class T_Group_Psionics( Base ):
    __tablename__ = 'Group_Psionics'
    Id_Group_Psionics  =  Column(Integer, primary_key=True,  autoincrement=True)
    Group_Psionics_Name  = Column(String(255) , unique =True ,index =True )     
      
 
"""


@dataclass
class GroupeREF:
    id_GroupeREF:int 
    name: str 
    typeGroup: str 
    Description: str 

    init_sqlalchemy_rcg_fr()
    init_sqlalchemy_rcg_gb()
        
    def Id_GroupeREF_fr(self, thisIdgroupe, thisName, thisTypeGroup, thisDescription) -> int:

        requete =  select(T_GroupeREF.name,T_GroupeREF.name ,T_GroupeREF.typeGroup,T_GroupeREF.Description).filter_by(name=thisName)
        
        #
        
        try :   
            resultat =  DBSession_rcg_fr.execute(requete).scalar_one()
            for   Id_GroupeREF, name, typeGroup, Description in   resultat :     
                self.id_GroupeREF = Id_GroupeREF
                self.name = name
                self.typeGroup= typeGroup
                self.Description= Description
                
        except  Exception as  NoResultFound:     
            
            self.update_fr() #mise à jour
            
            requete =  select(T_GroupeREF.Id_CCName,T_GroupeREF.name ,T_GroupeREF.typeGroup,T_GroupeREF.Description).filter_by(name=thisName).scalar_one()
            resultat =  DBSession_rcg_fr.execute(requete)
            
            for   Id_GroupeREF,name, typeGroup, Description in   resultat :     
                self.id_GroupeREF = Id_GroupeREF
                self.name = name
                self.typeGroup= typeGroup
                self.Description= Description
            return self.Id_GroupeREF
        except  Exception as erreur:
            print("Erreur:" , erreur)
        else:
            return self.Id_GroupeREF


       
    def Id_GroupeREF_gb(self, thisIdgroupe,thisName, thisTypeGroup, thisDescription) -> int:
        
        requete =  select(T_GroupeREF.Id_CCName,T_GroupeREF.name ,T_GroupeREF.typeGroup,T_GroupeREF.Description).filter_by(name=thisName).scalar_one()
        
        
        try :   
            resultat =  DBSession_rcg_gb.execute(requete)
            for   Id_GroupeREF, name, typeGroup, Description in   resultat :     
                self.id_GroupeREF = Id_GroupeREF
                self.name = name
                self.typeGroup= typeGroup
                self.Description= Description
                
        except  Exception as  NoResultFound:     
            self.update_gb() #mise à jour
            requete =  select(T_GroupeREF.Id_CCName,T_GroupeREF.name ,T_GroupeREF.typeGroup,T_GroupeREF.Description).filter_by(name=thisName).scalar_one()
            resultat =  DBSession_rcg_gb.execute(requete)
            
            for   Id_GroupeREF,name, typeGroup, Description in   resultat :     
                self.id_GroupeREF = Id_GroupeREF
                self.name = name
                self.typeGroup= typeGroup
                self.Description= Description
            return self.Id_GroupeREF
        except  Exception as erreur:
            print("Erreur:" , erreur)
        else:
            return self.Id_GroupeREF
    
   
    def update_fr(self):

        stmt = insert(T_GroupeREF).values(name = self.name , typeGroup= self.typeGroup , Description= self.Description)
   
        try:
            DBSession_rcg_fr.execute(stmt)
        except  Exception as erreur:
            print("Erreur:" , erreur)
            DBSession_rcg_fr.rollback()
        else:
            DBSession_rcg_fr.commit()
            
            
            
    def update_gb(self):

        stmt = insert(T_GroupeREF).values(name = self.name , typeGroup= self.typeGroup , Description= self.Description)
   
        try:
            DBSession_rcg_gb.execute(stmt)
        except  Exception as erreur:
            print("Erreur:" , erreur)
            DBSession_rcg_gb.rollback()
        else:
            DBSession_rcg_gb.commit()



"""    
    def Id_GroupeREF_gb(self, thisIdgroupe,thisName, thisTypeGroup, thisDescription) -> int:
        
        try :
            (self.Id_GroupeREF,self.name, self.typeGroup, self.Description) = DBSession_rcg_gb.execute(
                select(T_GroupeREF.Id_CCName,T_GroupeREF.name ,T_GroupeREF.typeGroup,T_GroupeREF.Description).filter_by(name=thisName))
        except  Exception as  NoResultFound:     
            self.update_gb(self) #insertion des données
            (self.Id_GroupeREF,self.name, self.typeGroup, self.Description) = DBSession_rcg_gb.execute(
                select(T_GroupeREF.Id_CCName,T_GroupeREF.name ,T_GroupeREF.typeGroup,T_GroupeREF.Description).filter_by(name=thisName))
            return self.Id_GroupeREF
        except  Exception as erreur:
            print("Erreur:" , erreur)
        else:
            return self.Id_GroupeREF
    
    def updateT_GroupeREF_gb(self):
        stmt = insert(T_GroupeREF).values(self.name,self.typeGroup,self.Description)
        try:
            DBSession_rcg_gb.execute(stmt)
        except  Exception as erreur:
            print("Erreur:" , erreur)
            DBSession_rcg_gb.rollback()
        else:
            DBSession_rcg_gb.commit()
"""         

class T_Category( Base ):
    __tablename__ = 'Category'
    Id_Category = Column(Integer, primary_key=True,  autoincrement=True)
    Nom_Category = Column(String(255) , unique =True ,index =True)
    Type_Category = Column(String(255) ) 

class T_Animal( Base ):
    __tablename__ = 'Animal'
    Id_Animal =  Column(Integer, primary_key=True,  autoincrement=True) 
    Nom_Animal = Column(String(255) , unique =True ,index =True )
    Point_de_Vie = Column(Integer)
    SDC = Column(Integer)
    MDC =  Column(Integer)
    Touche = Column(Integer)
    Parade = Column(Integer)
    Esquive = Column(Integer)
    Vitesse = Column(Integer)
    Abilite = Column(Text)
    Apr =Column(Integer)
    Categorie =Column(String(255) )
    Description =  Column(Text)
    

class T_Attaque_Animal( Base ):
    __tablename__ = 'Attaque_Animal'
    Id_Attaque  = Column(Integer, primary_key=True,  autoincrement=True)
    Id_Animal  = Column(Integer ,  ForeignKey(T_Animal.Id_Animal ))
    Arme = Column(String(255) )
    Degat = Column(String(255) )
    Description = Column(String(255) )

    Id_Animal_relation  = relationship('T_Animal', foreign_keys='T_Attaque_Animal.Id_Animal') # reference de relation table primeire identiant de la table secondaire


class T_Armes( Base ):
    __tablename__ = 'Armes'
    Id_Arme  =  Column(Integer, primary_key=True,  autoincrement=True)
    Nom_de_l_arme = Column(String(255) , unique =True ,index =True )
    WP = Column(String(255) )
    Poids = Column(String(255) )
    MCD  = Column(String(255) )
    SDC  = Column(String(255) )
    Cadence_de_tir =Column(BLOB)
    Portee_Effective =Column(BLOB) 
    Chargeur = Column(Text)
    Bonus  = Column(Text)
    CoutMarcheNoir  = Column(Text)
    Description  = Column(Text)
    Page = Column(String(255) )
    Class = Column(String(255) )
 


class T_Alignement( Base ):
    __tablename__ = 'Alignement'
    Id_Alignement  = Column(Integer, primary_key=True,  autoincrement=True)    
    Nom_Alignement = Column(String(255) , unique =True ,index =True )


class T_Caracteristique( Base ):
    __tablename__ = 'Caracteristique'
    Id_Caracteristique  = Column(Integer, primary_key=True,  autoincrement=True)       
    Nom = Column(String(255) , unique =True ,index =True )
    Alias = Column(String(255) , unique =True )
    Description = Column(String(255)  )  
    
class T_Classe( Base ):
    __tablename__ = 'Classe'
    Id_Classe = Column(Integer, primary_key=True,  autoincrement=True)    
    Nom_de_classe = Column(String(255) , unique =True ,index =True )
    Description = Column(String(255)   )  
 
class T_Creature_Intelligente( Base ):
    __tablename__ = 'Creature_Intelligente'
    ID_Creature  = Column(Integer, primary_key=True,  autoincrement=True)    
    Nom_de_la_creature = Column(String(255) , unique =True ,index =True )
    Intelligence  = Column(Integer  )
    Force  = Column(Integer)
    Dexterite  = Column(Integer)
    Eph  = Column(Integer)
    EME   = Column(Integer)
    Vitesse  = Column(Integer)
    Type_de_deplassement = Column(Integer)
    Facteur_d_Horreur  = Column(Integer)
    Point_de_Vie = Column(Integer)
    SDC  = Column(Integer)
    MDC  = Column(Integer)
    Touche = Column(Integer)
    Parade  = Column(Integer)
    Esquive  = Column(Integer)
    Abilite= Column(String(255) )
    Categorie = Column(String(255) )
    Description = Column(Text) 

class T_Degat( Base ):
    __tablename__ = 'Degat'
    Id_Degat = Column(Integer, primary_key=True,  autoincrement=True)
    Attaque = Column(String(255) , unique =True ,index =True )
    Degat = Column(Integer)
    Type_de_degat = Column(String(255))




    
class T_Type_de_Mutation( Base ):
    __tablename__ = 'Type_de_Mutation'
    Id_Type_de_Mutation  = Column(Integer, primary_key=True,  autoincrement=True)    
    Nom = Column(String(255) , unique =True ,index =True ) 
    Description  = Column(Text)
  
class T_Category_Spells( Base ):
    __tablename__ = 'Category_Spells'
    Id_Category_Spells  = Column(Integer, primary_key=True,  autoincrement=True)
    Name = Column(String(255) , unique =True ,index =True )
    Description  = Column(Text)

class T_Spells( Base ):
    __tablename__ = 'Spells'
    Id_Spells  = Column(Integer, primary_key=True,  autoincrement=True)
    SpellName = Column(String(255) , unique =True ,index =True )
    Range  = Column(Text)
    Duration = Column(Integer, default =0)
    SavingThrow = Column(Text)
    Cost = Column(Text)
    Description  = Column(Text)
    Limits = Column(String(20))
    Id_Category_Spells  =  Column(Integer ,  ForeignKey(T_Category_Spells.Id_Category_Spells ))
    CostType = Column(String(10) , unique =True ,index =True )
    



 
class T_Skills( Base ):
    __tablename__ = 'Skills'
    Id_Skills = Column(Integer, primary_key=True,  autoincrement=True)
    Id_GroupeREF =  Column(Integer, ForeignKey(T_GroupeREF.Id_GroupeREF))
    Description = Column(Text)      
    Requires = Column(Text)  
    BasePercent = Column(Integer, default = 0)
    PercentPerLevel = Column(Integer, default = 0)
    
class T_Skill_PreReqs( Base ):
    __tablename__ = 'Skill_PreReqs'
    Id_Prerequis = Column(Integer, primary_key=True,  autoincrement=True)
    ID_Skills =  Column(Integer, ForeignKey(T_Skills.Id_Skills)  )   
    Id_Skill_prerequis =  Column(Integer, ForeignKey(T_Skills.Id_Skills)  )
    Id_Skill_prerequis_2 =  Column(Integer, ForeignKey(T_Skills.Id_Skills), default = null )
    
    
"""
CREATE TABLE Skill_Prerequis (
    Id_Prerequis INTEGER NOT NULL, 
    Id_Skill INTEGER NOT NULL,
    Id_Skill_prerequis INTEGER  NOT NULL,
    Id_Skill_prerequis_2 INTEGER  NULL,
    PRIMARY KEY (Id_Prerequis) ,
    FOREIGN KEY(Id_Skill) REFERENCES Skill  (Id_Skill) ,
    FOREIGN KEY(Id_Skill_prerequis) REFERENCES Skill  (Id_Skill)  ,
    FOREIGN KEY(Id_Skill_prerequis_2) REFERENCES Skill  (Id_Skill)  
);



 

Basic Electronics|Electrical Engineering|
Electrical Engineer                     |
Mathematics: Advanced|Mathematics: Basic|

"""
       
class T_Bionics( Base ):
    __tablename__ = 'Bionics'
    Id_Bionics =  Column(Integer, primary_key=True,  autoincrement=True) 
    Nom_Bionics = Column(String(255) , unique =True ,index =True )
    Id_Category_bionic  =  Column(Integer, ForeignKey(T_Category.Id_Category ))
    Cost = Column(Float ,default = 0.0)
    Cat =  Column(String(1))
    Location =  Column(String(255)) 
    Description =  Column(Text)
    
class T_Bionic_Weapon( Base ):
    __tablename__ = 'Bionic_Weapon'
    Id_Bionic_Weapon =  Column(Integer, primary_key=True,  autoincrement=True) 
    ItemName = Column(String(255) , unique =True ,index =True )
    Damage =  Column(String(255)) 
    Effect =  Column(String(255))    
    Payload  =  Column(String(255))    
    ROF =  Column(String(255) , default ="Equal to Attacks per round") 
    Range   =  Column(String(255))    
    Id_Category_bionic  =  Column(Integer, ForeignKey(T_Category.Id_Category ))
 
 
class T_Power_ArmorBase(Base ):
    __tablename__ = 'Power_Armor'
    Id_Power_Armor  =  Column(Integer, primary_key=True,  autoincrement=True) 
    VehicleName = Column(String(255) , unique =True ,index =True )
    Description  =  Column(Text)
    Model  =  Column(Text)
    Classe  =  Column(Text)
    Crew  =  Column(Text)
    Notes  =  Column(Text)
    GroundSpeed   =  Column(Text)
    FlySpeed  =  Column(Text)
    Flyrange  =  Column(Text)
    Height  =  Column(Text)
    Width  =  Column(Text)
    Length  =  Column(Text)
    Weight  =  Column(Text)
    Cargo  =  Column(Text)
    PowerSystem  =  Column(Text)
    Classification =Column(String(255)) 
    BlackMarketCost  =  Column(Text)
    PAL = Column(String(1)) 
    
 
class T_Power_Armor_MDC(Base ):
    __tablename__ = 'Power_Armor_MDC' 
    Id_PA_MCD  =  Column(Integer, primary_key=True,  autoincrement=True) 
    Location   =Column(String(255)) 
    MCD = Column(Integer)
    Id_Power_Armor  =  Column(Integer, ForeignKey(T_Power_ArmorBase.Id_Power_Armor)) 
    # Id_T_PA_PAMDC  = relationship('T_Power_ArmorBase', foreign_keys='T_Power_Armor_MDC.Id_Power_Armor') 
    # reference de relation table primeire identiant de la table secondaire  
    # REFERENCES Power_Armor (Id_Power_Armor) ON DELETE CASCADE ON UPDATE CASCADE
 
class T_Power_Armor_Weapons(Base ):
    __tablename__ = 'Power_Armor_Weapons' 
    Id_PA_Weapons  =  Column(Integer, primary_key=True,  autoincrement=True)  
    Weapon  =  Column(Text)
    Description =  Column(Text)
    PrimaryPurpose  =  Column(Text)
    SecondaryPurpose  =  Column(Text)
    MissileType  =  Column(Text)
    MegaDamage  =  Column(Text)
    Range  =  Column(Text)
    RateofFir  =  Column(Text)
    Payload  =  Column(Text)
    Id_Power_Armor  =  Column(Integer, ForeignKey(T_Power_ArmorBase.Id_Power_Armor)) 
    #Id_T_PA_PAW  = relationship('T_Power_Armor_MDC', foreign_keys='T_Power_Armor_MDC.Id_PA_MCD') 
    
    # reference de relation table primeire identiant de la table secondaire  REFERENCES Power_Armor (Id_Power_Armor) ON DELETE CASCADE ON UPDATE CASCADE


 
     
class T_CC( Base ):
    __tablename__ = 'cc'
    Id_CCName  =  Column(Integer, primary_key=True,  autoincrement=True) 
    CCName  = Column(String(255) , unique =True ,index =True ) 
    CCType  = Column(String(1) )
    ISPLevel  = Column(String(50) )
    PPELevel  = Column(String(50) )
    MDCLevel  = Column(String(50) )
    MaxHP  = Column(Float , default = 0.0)
    MinHP  = Column(Float , default = 0.0)
    MaxSDC  = Column(Float , default = 0.0)
    MinSDC  = Column(Float , default = 0.0)
    MaxMDC  = Column(Float , default = 0.0)
    MinMDC  = Column(Float , default = 0.0)
    MaxPPE  = Column(Float , default = 0.0)
    MinPPE  = Column(Float , default = 0.0)
    MaxISP  = Column(Float , default = 0.0)
    MinISP  = Column(Float , default = 0.0)
    MaxIQ  = Column(Integer)
    MinIQ  = Column(Integer)
    MaxMa  = Column(Integer)
    MinMa  = Column(Integer)
    MaxMe  = Column(Integer)
    MinMe  = Column(Integer)
    MaxPs  = Column(Integer)
    MinPs  = Column(Integer)
    MaxPp  = Column(Integer)
    MinPp  = Column(Integer)
    MaxPe  = Column(Integer)
    MinPe  = Column(Integer)
    MaxPb  = Column(Integer)
    MinPb  = Column(Integer)
    MaxSpd  = Column(Integer)
    MinSpd  = Column(Integer)
    NoLang  = Column(Integer)
    NoWp  = Column(Integer)
    American  = Column(Integer)
    Dragonese  = Column(Integer)
    NoRSkills  = Column(Integer)
    NoSSkills  = Column(Integer)
    RequiredWP1  = Column(String(50) )
    RequiredWP2  = Column(String(50) )
    RequiredWP3  = Column(String(50) )
    RequiredWP4  = Column(String(50) )
    ReqSkillCat1  = Column(String(50) )
    ReqSkillCat2  = Column(String(50) )
    ReqSkillCat3  = Column(String(50) )
    ReqSkillNum1  = Column(Integer , default = 0.0)
    ReqSkillNum2  = Column(Integer , default = 0.0)
    ReqSkillNum3  = Column(Integer , default = 0.0)
    HTHBasic  = Column(Integer , default = 0.0)
    HTHExpert  = Column(Integer , default = 0.0)
    HTHMartialArts  = Column(Integer , default = 0.0)
    HTHAssassin  = Column(Integer , default = 0.0)
    NAwHTH  = Column(Float)
    NAintHTH  = Column(String(50) )
    AncientRq  = Column(Boolean )
    ModernRq  = Column(Boolean )
    PilotRq  = Column(Boolean ) 
    AncientNo  = Column(Integer)
    ModernNo  = Column(Integer)
    PilotNo  = Column(Integer)
    SkillSelection  = Column(String(50) )
    Description  = Column(Text)
    RSkillBonus  = Column(Integer)
    Credits  = Column(Text)
    BMCredits  = Column(Text)
    PowerType = Column(Text)
    Book  = Column(Text)
    Cybernetics  = Column(Text)
    Bionics = Column(Text)
    
class T_CCR_Progression( Base ):
    __tablename__ = 'CCR_Progression'
    Id_CCR_Progression  =  Column(Integer, primary_key=True,  autoincrement=True) 
    Id_CCName  =  Column(Integer  ,  ForeignKey(T_CC.Id_CCName ))
    Level     = Column(Integer, default =0)
    NoRSkills     = Column(Integer, default =0)
    NoSSkills     = Column(Integer, default =0)
    NoWP     = Column(Integer, default =0)
    NoSpells     = Column(Integer, default =0)
    NoESpells     = Column(Integer, default =0)
    NoESpellsAir     = Column(Integer, default =0)
    NoESpellsFire     = Column(Integer, default =0)
    NoESpellsWater     = Column(Integer, default =0)
    NoESpellsEarth     = Column(Integer, default =0)
    NoPsionics     = Column(Integer, default =0)
    NoGenPsionics     = Column(Integer, default =0)
    NoPsiSensitive     = Column(Integer, default =0)
    NoPsiPhysical     = Column(Integer, default =0)
    NoPsiHealing     = Column(Integer, default =0)
    NoPsiSuper     = Column(Integer, default =0)
    SpellLevels     = Column(Integer, default =0)
    MinLevel     = Column(Integer, default =0)
    NoSmpWeapon     = Column(Integer)
    NoMagWeapon     = Column(Integer)
    NoAnimal     = Column(Integer)
    NoMonster     = Column(Integer)
    NoPower     = Column(Integer)



class T_CC_Abilities( Base ):
    __tablename__ = 'CC_Abilities'
    Id_CC_Abilities  =  Column(Integer, primary_key=True,  autoincrement=True) 
    Id_CCName  =  Column(Integer  ,  ForeignKey(T_CC.Id_CCName ))
    Ability = Column(Text )
 
class T_CC_RSBonuses( Base ):
    __tablename__ = 'CC_RSBonuses'
    Id_CC_RSBonuses  =  Column(Integer, primary_key=True,  autoincrement=True) 
    Id_CCName  =  Column(Integer  ,  ForeignKey(T_CC.Id_CCName ))
    Grouping = Column(Text )
    BonusPercentage = Column(Integer)


class T_CC_RacialSkills( Base ):
    __tablename__ = 'CC_RacialSkills'
    Id_CC_RacialSkills  =  Column(Integer, primary_key=True,  autoincrement=True) 
    Id_CCName  =  Column(Integer  ,  ForeignKey(T_CC.Id_CCName ))   
    
 
    
class T_CC_Knowledge( Base ):
    __tablename__ = 'CC_Knowledge'
    Id_CC_Knowledge  =  Column(Integer, primary_key=True,  autoincrement=True) 
    Id_CCName  =  Column(Integer  ,  ForeignKey(T_CC.Id_CCName ))   
    LevelGained = Column(Integer)
    Id_Groupe_Knowledge = Column(Integer  ,  ForeignKey(T_GroupeREF.Id_GroupeREF))   
    Param1  = Column(String(255) )
    Param1Amount  = Column(Integer)
    Param2  = Column(String(255) )
    Param2Amount  = Column(Integer)   
    Param3 = Column(String(255) )
    Param3Amount  = Column(Integer)    
    Param4  = Column(String(255) )
    Param4Amount  = Column(Integer)
    Param5  = Column(String(255) )
    Param5Amount  = Column(Integer)
 

class T_CC_Psionics( Base ):
    __tablename__ = 'CC_Psionics'
    Id_CC_Psionics  =  Column(Integer, primary_key=True,  autoincrement=True) 
    Id_CCName  =  Column(Integer  ,  ForeignKey(T_CC.Id_CCName ))   
    Psionics   = Column(String(1) , default = 'R')
    NoHealing    = Column(Integer, default =0)
    NoSensitive    = Column(Integer, default =0)
    NoPhysical    = Column(Integer, default =0)
    NoSuper    = Column(Integer, default =0)
    NoPsionics    = Column(Integer, default =0)


class T_Psionics( Base ):
    __tablename__ = 'Psionics'
    Id_CC_Psionics  =  Column(Integer, primary_key=True,  autoincrement=True)  
    Id_GroupeREF =  Column(Integer  ,  ForeignKey(T_GroupeREF.Id_GroupeREF )) 
    Range  = Column(Text)
    Duration  = Column(Text)
    SavingThrow  = Column(Text)
    Cost  = Column(Text)
    LengthofTrance = Column(Text)
    Description  = Column(Text)
    PAL =Column(String(1)) 
    Page =Column(String(37)) 
    Category = Column(String(255) , default = 'Psionic' )
    CostType=Column(String(255)) 

class T_CC_Psionics_Given( Base ):
    __tablename__ = 'CC_Psionics_Given'
    Id_CC_Psionics_Given =  Column(Integer, primary_key=True,  autoincrement=True) 
    Id_CCName  =  Column(Integer  ,  ForeignKey(T_CC.Id_CCName ))   
    Id_CC_Psionics  =  Column(Integer ,  ForeignKey(T_Psionics.Id_CC_Psionics )) 


class T_CC_Psionics_Selections( Base ):
    __tablename__ = 'CC_Psionics_Selections'
    Id_CC_Psionics_Given =  Column(Integer, primary_key=True,  autoincrement=True) 
    Id_CCName  =  Column(Integer  ,  ForeignKey(T_CC.Id_CCName ))   
    Id_CC_Psionics  =  Column(Integer ,  ForeignKey(T_Psionics.Id_CC_Psionics )) 
  
"""
-- `CC_Psionics_Selections` definition

"""    
class T_CCR_Bonuses( Base ):
    __tablename__ = 'CCR_Bonuses'
    Id_CCR_Bonuses  =  Column(Integer, primary_key=True,  autoincrement=True) 
    Id_CCName  =  Column(Integer  ,  ForeignKey(T_CC.Id_CCName ))
    SavePsychic  =  Column(Integer) 
    SaveComaDeath  =  Column(Integer) 
    SaveMagic  =  Column(Integer) 
    SavePoison  =  Column(Integer)
    SaveMindControl  =  Column(Integer)
    SaveToxins  =  Column(Integer)
    BonusTrust  =  Column(Integer)
    BonusCharm  =  Column(Integer)
    BonusHTHDamage  =  Column(Integer)
    BonusParry  =  Column(Integer)
    BonusDodge  =  Column(Integer)
    BonusStrike  =  Column(Integer)
    BonusPullPunch  =  Column(Integer)
    BonusRoll  =  Column(Integer)
    BonusInitiative  =  Column(Integer)
    AttacksMelee  =  Column(Integer)
    Horror  =  Column(Integer)
    IQ = Column(String(13))
    MA = Column(String(13))
    ME = Column(String(13))
    PS = Column(String(13))
    PP = Column(String(13))
    PE = Column(String(13))
    PB = Column(String(13))
    Spd = Column(String(13))
    SDC = Column(String(13))
    MDC = Column(String(13))
    HP = Column(String(13))
    ISP = Column(String(13))
    PPE = Column(String(13))
    CommBonus =  Column(Integer, default = 0)
    DomBonus =  Column(Integer, default = 0) 
    ElecBonus =  Column(Integer, default = 0)
    EspBonus =  Column(Integer, default = 0) 
    LangBonus =  Column(Integer, default = 0)
    MechBonus =  Column(Integer, default = 0)
    MedBonus =  Column(Integer, default = 0)
    MilBonus =  Column(Integer, default = 0)
    PhyBonus =  Column(Integer, default = 0)
    PilotBonus =  Column(Integer, default = 0)
    PRBonus =  Column(Integer, default = 0)
    RogueBonus =  Column(Integer, default = 0)
    SciBonus =  Column(Integer, default = 0)
    TechBonus =  Column(Integer, default = 0)
    WildBonus =  Column(Integer, default = 0)
   
class T_Vehicles( Base ):
    __tablename__ = 'Vehicles'
    Id_Vehicles  = Column(Integer, primary_key=True,  autoincrement=True)    
    Nom_du_Vehicule = Column(String(255) , unique =True ,index =True ) 
    Description  = Column(Text)
    Modele   = Column(Text)
    Classe   = Column(Text)
    Equipage   = Column(Text)
    Notes   = Column(Text)
    Vitesse_au_sol   = Column(Text)
    Vitesse_de_vol   = Column(Text)
    Flyrange   = Column(Text)
    Hauteur    = Column(Text)
    Largeur    = Column(Text)
    Longueur   = Column(Text)
    Poids   = Column(Text)
    Cargo   = Column(Text)
    Systeme_de_propulsion   = Column(Text)
    CoutMarcheNoir   = Column(Text)
    Classification  = Column(String(6))
    Page  = Column(String(50) )

class T_Vehicles_MDC(Base ):
    __tablename__ = 'Vehicles_MDC' 
    Id_V_MCD  =  Column(Integer, primary_key=True,  autoincrement=True) 
    Location   =Column(String(255)) 
    MCD = Column(Integer)
    Id_Vehicles  =  Column(Integer, ForeignKey(T_Vehicles.Id_Vehicles)) 
  
class T_Vehicles_Options(Base ):
    __tablename__ = 'Vehicles_Options' 
    Id_V_Op  =  Column(Integer, primary_key=True,  autoincrement=True) 
    Options  = Column(String(50)) 
    Cost     = Column(Float , default =0.0)
    Id_Vehicles  =  Column(Integer, ForeignKey(T_Vehicles.Id_Vehicles))  

class T_Vehicles_Weapons(Base ):
    __tablename__ = 'Vehicles_Weapons' 
    Id_V_WP  =  Column(Integer, primary_key=True,  autoincrement=True) 
    Weapon = Column(Text)
    Description = Column(Text)
    PrimaryPurpose = Column(Text)
    SecondaryPurpose = Column(Text)
    MissileType = Column(Text)
    MegaDamage = Column(Text)
    Range = Column(Text)
    RateofFire = Column(Text)
    Payload = Column(Text)
    Id_Vehicles = Column(Integer, ForeignKey('Vehicles.Id_Vehicles'))
    Vehicles = relationship(T_Vehicles)    

class T_H2H(Base ):
    __tablename__ = 'H2H' 
    Id_SkillName  =  Column(Integer, primary_key=True,  autoincrement=True) 
    Level =  Column(Integer)
    Attacks =  Column(Integer,default =0)
    Initiative=  Column(Integer,default =0)
    Strike=  Column(Integer,default =0)
    Parry =  Column(Integer,default =0)
    Dodge =  Column(Integer,default =0)
    RollWith =  Column(Integer,default =0)
    PullPunch  =  Column(Integer,default =0)
    SDC  =  Column(Integer,default =0)
    PP   =  Column(Integer,default =0)
    PE   =  Column(Integer,default =0)     
    PS   =  Column(Integer,default =0)
    ME   =  Column(Integer,default =0)
    MA   =  Column(Integer,default =0)
    Damage   =  Column(Integer,default =0)
    Attack  = Column(String(255)) 
    Effect1  = Column(String(255)) 
    Effect2  = Column(String(255)) 

def init_sqlalchemy_rcg_fr():  # Base sqllite-fr
    global engine_rcg_fr
    global Base_rcg_fr 
    global DBSession_rcg_fr 

    Base_rcg_fr = declarative_base()
    DBSession_rcg_fr = scoped_session(sessionmaker())
    BaseSqllite_fr = 'baseGenFRS.db'
    dbname = 'sqlite:///' + BaseSqllite_fr
    engine_rcg_fr = create_engine(dbname, echo=False)
    
    Base.metadata.drop_all(engine_rcg_fr)       # drop des tables
    Base.metadata.create_all(engine_rcg_fr)      # uniquement � la creation installe les tables
    DBSession_rcg_fr.remove()
    DBSession_rcg_fr.configure(bind=engine_rcg_fr, autoflush=False, expire_on_commit=False)

def init_sqlalchemy_rcg_gb():  # Base sqllite-fr
    global engine_rcg_gb
    global Base_rcg_gb 
    global DBSession_rcg_gb 

    Base_rcg_gb = declarative_base()
    DBSession_rcg_gb = scoped_session(sessionmaker())
    BaseSqllite_gb = 'baseGengb.db'
    dbname = 'sqlite:///' + BaseSqllite_gb
    engine_rcg_gb = create_engine(dbname, echo=False)
    
    Base.metadata.drop_all(engine_rcg_gb)       # drop des tables
    Base.metadata.create_all(engine_rcg_gb)      # uniquement � la creation installe les tables
    DBSession_rcg_gb.remove()
    DBSession_rcg_gb.configure(bind=engine_rcg_gb, autoflush=False, expire_on_commit=False)
    


def table_Category(sql_requete):
        print("Creer et Charger Table Category")
        cur_BaseOrigine.execute(sql_requete )
        result = cur_BaseOrigine.fetchall()  # fetchall() : r�cup�re toutes les lignes qui correspondent aux param�tres d�finis.
        for Category ,   in result:
            stmt = insert(T_Category).values(Nom_Category = Category , Type_Category='bionic')

            try:
                DBSession_rcg_fr.execute(stmt)
            except  Exception as erreur:
                print("Erreur:" , erreur)
                DBSession_rcg_fr.rollback()
            else:
                DBSession_rcg_fr.commit()

            try:
                DBSession_rcg_gb.execute(stmt)
            except  Exception as erreur:
                print("Erreur:" , erreur)
                DBSession_rcg_gb.rollback()
            else:
                DBSession_rcg_gb.commit()


def table_bionic(sql_requete):
    print("Creer et Charger Table bionic ")
    cur_BaseOrigine.execute(sql_requete ) #construction
    result = cur_BaseOrigine.fetchall()  #fetchall() : récupère toutes les lignes qui correspondent aux paramêtres définis.
    for o_Category, o_ItemName, o_Cost, o_Cat, o_Location, o_Description    in result:
        #recupeer la catégorie
        O_Id_Category_bionic = DBSession_rcg_fr.execute(select(T_Category.Id_Category).where(T_Category.Nom_Category == o_Category)).first()[0]
        stmt =  insert(T_Bionics).values( Nom_Bionics = o_ItemName , Id_Category_bionic  = O_Id_Category_bionic , 
                                           Cost  = o_Cost , Cat = o_Cat ,  Location  = o_Location ,  Description  = o_Description ) 

        try:
            DBSession_rcg_fr.execute(stmt)
        except  Exception as erreur:
            print("Erreur:" , erreur)
            DBSession_rcg_fr.rollback()
        else:
            DBSession_rcg_fr.commit()

        try:
            DBSession_rcg_gb.execute(stmt)
        except  Exception as erreur:
            print("Erreur:" , erreur)
            DBSession_rcg_gb.rollback()
        else:
            DBSession_rcg_gb.commit()
            
def table_Bionic_Weapon(sql_requete): 
        cur_BaseOrigine.execute(sql_requete)
        try:
            print("creer et Charger Table Bionic_Weapon  ")
            result = cur_BaseOrigine.fetchall()  # fetchall() : r�cup�re toutes les lignes qui correspondent aux param�tres d�finis.
            for o_ItemName, o_Damage, o_Effect, o_Payload, o_ROF, o_Range  in result:
                
                stmt =  insert(T_Bionic_Weapon).values(ItemName = o_ItemName , Damage = o_Damage,  Effect= o_Effect , 
                                                       Payload = o_Payload ,ROF= o_ROF , Range = o_Range)
                try:
                    DBSession_rcg_fr.execute(stmt)
                except  Exception as erreur:
                    print("Erreur:" , erreur)
                    DBSession_rcg_fr.rollback()
                else:
                    DBSession_rcg_fr.commit()
               
                try:
                    DBSession_rcg_gb.execute(stmt)
                except  Exception as erreur:
                    print("Erreur:" , erreur)
                    DBSession_rcg_gb.rollback()
                else:
                    DBSession_rcg_gb.commit()
                                
        except  Exception as erreur:
            print("Erreur:" , erreur)

def table_CC(sql_requete):
    print("Charger Table CC")
    cur_BaseOrigine.execute(sql_requete)
    resultat = cur_BaseOrigine.fetchall()  # fetchall() :  

    for _CCName , _CCType , _ISPLevel ,  _PPELevel ,  _MDCLevel ,  _MaxHP ,  _MinHP , _MaxSDC , \
    _MinSDC , _MaxMDC ,  _MinMDC , _MaxPPE , _MinPPE , _MaxISP , _MinISP , _MaxIQ ,  _MinIQ , \
    _MaxMa ,  _MinMa , _MaxMe , _MinMe , _MaxPs , _MinPs , _MaxPp ,  _MinPp , _MaxPe , _MinPe , \
    _MaxPb , _MinPb , _MaxSpd , _MinSpd , _NoLang , _NoWp , _American , _Dragonese , _NoRSkills , \
    _NoSSkills , _RequiredWP1 , _RequiredWP2 , _RequiredWP3 , _RequiredWP4 , _ReqSkillCat1 , \
    _ReqSkillCat2 , _ReqSkillCat3 , _ReqSkillNum1 , _ReqSkillNum2 , _ReqSkillNum3 , _HTHBasic , \
    _HTHExpert , _HTHMartialArts , _HTHAssassin , _NAwHTH , _NAintHTH , _AncientRq , _ModernRq ,  \
    _PilotRq ,_AncientNo , _ModernNo , _PilotNo ,  _SkillSelection , _Description ,  \
    _RSkillBonus , _Credits , _BMCredits , _PowerType , _Book , _Cybernetics , _Bionics in resultat:
        
        stmt = insert(T_CC).values( CCName = _CCName , CCType = _CCType , ISPLevel = _ISPLevel , 
                PPELevel = _PPELevel , MDCLevel = _MDCLevel , MaxHP = _MaxHP , MinHP = _MinHP ,
                MaxSDC = _MaxSDC , MinSDC = _MinSDC , MaxMDC = _MaxMDC , MinMDC = _MinMDC , MaxPPE = _MaxPPE ,
                MinPPE = _MinPPE , MaxISP = _MaxISP , MinISP = _MinISP , MaxIQ = _MaxIQ , 
                MinIQ = _MinIQ , MaxMa = _MaxMa , MinMa = _MinMa , MaxMe = _MaxMe , 
                MinMe = _MinMe , MaxPs = _MaxPs , MinPs = _MinPs , MaxPp = _MaxPp , 
                MinPp = _MinPp , MaxPe = _MaxPe , MinPe = _MinPe , MaxPb = _MaxPb ,
                MinPb = _MinPb , MaxSpd = _MaxSpd , MinSpd = _MinSpd , NoLang = _NoLang ,
                NoWp = _NoWp , American = _American , Dragonese = _Dragonese ,  NoRSkills = _NoRSkills ,
                NoSSkills = _NoSSkills , RequiredWP1 = _RequiredWP1 , RequiredWP2 = _RequiredWP2 , 
                RequiredWP3 = _RequiredWP3 , RequiredWP4 = _RequiredWP4 , ReqSkillCat1 = _ReqSkillCat1 , 
                ReqSkillCat2 = _ReqSkillCat2 , ReqSkillCat3 = _ReqSkillCat3 , ReqSkillNum1 = _ReqSkillNum1 , 
                ReqSkillNum2 = _ReqSkillNum2 , ReqSkillNum3 = _ReqSkillNum3 , HTHBasic = _HTHBasic , 
                HTHExpert = _HTHExpert , HTHMartialArts = _HTHMartialArts , HTHAssassin = _HTHAssassin ,
                NAwHTH = _NAwHTH , NAintHTH = _NAintHTH , AncientRq = _AncientRq , ModernRq = _ModernRq )

        try:
            DBSession_rcg_fr.execute(stmt)
        except  Exception as erreur:
            print("Erreur:" , erreur)
            DBSession_rcg_fr.rollback()
        else:
            DBSession_rcg_fr.commit()

        try:
            DBSession_rcg_gb.execute(stmt)
        except  Exception as erreur:
            print("Erreur:" , erreur)
            DBSession_rcg_gb.rollback()
        else:
            DBSession_rcg_gb.commit()
 

def table_CCR_Progression(sql_requete):

    cur_BaseOrigine.execute(sql_requete)
    print("Charger CCR_Progression")
    resultat = cur_BaseOrigine.fetchall()  # fetchall() :  
     
    for o_CCName , o_Level , o_NoRSkills , o_NoSSkills , o_NoWP , o_NoSpells , o_NoESpells , o_NoESpellsAir , o_NoESpellsFire , o_NoESpellsWater , \
    o_NoESpellsEarth , o_NoPsionics , o_NoGenPsionics , o_NoPsiSensitive , o_NoPsiPhysical , o_NoPsiHealing , o_NoPsiSuper , o_SpellLevels ,  \
    o_MinLevel , o_NoSmpWeapon , o_NoMagWeapon , o_NoAnimal , o_NoMonster , o_NoPower in resultat:
        o_Id_CCName = DBSession_rcg_fr.execute(select(T_CC.Id_CCName).where(T_CC.CCName ==  o_CCName)).first()[0]
   
        stmt = insert(T_CCR_Progression).values( Id_CCName =o_Id_CCName , Level = o_Level , NoRSkills = o_NoRSkills ,
            NoSSkills = o_NoSSkills , NoWP = o_NoWP , NoSpells = o_NoSpells ,
            NoESpells = o_NoESpells   , NoESpellsAir = o_NoESpellsAir ,
            NoESpellsFire = o_NoESpellsFire, NoESpellsWater = o_NoESpellsWater ,
            NoESpellsEarth = o_NoESpellsEarth, NoPsionics = o_NoPsionics ,
            NoGenPsionics = o_NoGenPsionics , NoPsiSensitive = o_NoPsiSensitive ,
            NoPsiPhysical = o_NoPsiPhysical , NoPsiHealing = o_NoPsiHealing ,
            NoPsiSuper = o_NoPsiSuper , SpellLevels = o_SpellLevels ,
            MinLevel = o_MinLevel , NoSmpWeapon = o_NoSmpWeapon ,
            NoMagWeapon = o_NoMagWeapon , NoAnimal = o_NoAnimal ,
            NoMonster = o_NoMonster, NoPower = o_NoPower )
        try:
            DBSession_rcg_fr.execute(stmt)
        except  Exception as erreur:
            print("Erreur:" , erreur)
            DBSession_rcg_fr.rollback()
        else:
            DBSession_rcg_fr.commit()


        try:
            DBSession_rcg_gb.execute(stmt)
        except  Exception as erreur:
            print("Erreur:" , erreur)
            DBSession_rcg_gb.rollback()
        else:
            DBSession_rcg_gb.commit()
            
def table_CC_Abilities(sql_requete):
    cur_BaseOrigine.execute(sql_requete)
 
    print("Charger  CC_Abilities")
    resultat = cur_BaseOrigine.fetchall()  # fetchall() :  
     
    for o_CCName ,  o_Ability in resultat:
        o_Id_CCName= None
        # Base Française
        #print(f'o_Id_CCName : {o_Id_CCName} / o_CCName {o_CCName} -  o_Ability  :{o_Ability}        ')
        try:
            o_Id_CCName = DBSession_rcg_fr.execute(select(T_CC.Id_CCName).filter_by(CCName = o_CCName)).scalar_one()

        except  Exception as  NoResultFound: 
            
            print("cas  Cyber Horsemen of Ixion base fr ")
            stmt = insert(T_CC).values( CCName = o_CCName  ) # ajout d d'un CC inconnu de la base CC
            # 1seul cas  Cyber Horsemen of Ixion
            try:
                DBSession_rcg_fr.execute(stmt)
            except  Exception as erreur:
                print("Erreur base fr insert new T_CC" , erreur)
            else:
                DBSession_rcg_fr.commit()
            finally:
                o_Id_CCName = DBSession_rcg_fr.execute(select(T_CC.Id_CCName).filter_by(CCName = o_CCName)).scalar_one()
        else:
            # cécuperer Id_CCName venant d'etre creer
            o_Id_CCName = DBSession_rcg_fr.execute(select(T_CC.Id_CCName).filter_by(CCName = o_CCName)).scalar_one()
                    
            stmt = insert(T_CC_Abilities).values( Id_CCName = o_Id_CCName ,  Ability = o_Ability  )
            try:
                DBSession_rcg_fr.execute(stmt)
            except  Exception as erreur:
                print("Erreur base fr:" , erreur)
                DBSession_rcg_fr.rollback()
            else:
                DBSession_rcg_fr.commit()
        # Base anglaise
      
        try:
            o_Id_CCName = DBSession_rcg_gb.execute(select(T_CC.Id_CCName).filter_by(CCName = o_CCName)).scalar_one()

         # Base anglaise
        except  Exception as  NoResultFound: 
            
            print("cas  Cyber Horsemen of Ixion base gb ")
            stmt = insert(T_CC).values( CCName = o_CCName  ) # ajout d d'un CC inconnu de la base CC
            # seul cas  Cyber Horsemen of Ixion
            try:
                DBSession_rcg_gb.execute(stmt)
            except  Exception as erreur:
                print("Erreur base fr insert new T_CC" , erreur)
            else:
                DBSession_rcg_gb.commit()
            finally: # recuperer T_CC.Id_CCName de l'insertion 
                o_Id_CCName = DBSession_rcg_gb.execute(select(T_CC.Id_CCName).filter_by(CCName = o_CCName)).scalar_one()
        else:
            # cécuperer Id_CCName venant d'etre creer

            o_Id_CCName = DBSession_rcg_gb.execute(select(T_CC.Id_CCName).filter_by(CCName = o_CCName)).scalar_one()
                    
            stmt = insert(T_CC_Abilities).values( Id_CCName = o_Id_CCName ,  Ability = o_Ability  )
            try:
                DBSession_rcg_gb.execute(stmt)
            except  Exception as erreur:
                print("Erreur base gb:" , erreur)
                DBSession_rcg_gb.rollback()
            else:
                DBSession_rcg_gb.commit()
      
      

def table_CCR_Bonuses(sql_requete):
        cur_BaseOrigine.execute(sql_requete)
        print("Charger Table CCR_Bonuses")
        resultat = cur_BaseOrigine.fetchall()  # fetchall() :  
     
        for o_CCName , o_SavePsychic,  o_SaveComaDeath , o_SaveMagic,  o_SavePoison, o_SaveMindControl,  o_SaveToxins,\
         o_BonusTrust, o_BonusCharm, o_BonusHTHDamage, o_BonusParry, o_BonusDodge, o_BonusStrike, o_BonusPullPunch,\
         o_BonusRoll, o_BonusInitiative, o_AttacksMelee, o_Horror, o_IQ, o_MA, o_ME, o_PS, o_PP, o_PE, o_PB,\
         o_Spd, o_SDC, o_MDC, o_HP, o_ISP, o_PPE, o_CommBonus, o_DomBonus, o_ElecBonus, o_EspBonus, o_LangBonus,\
         o_MechBonus, o_MedBonus, o_MilBonus, o_PhyBonus, o_PilotBonus, o_PRBonus, o_RogueBonus, o_SciBonus,\
         o_TechBonus, o_WildBonus in resultat:

            #o_Id_CCName = DBSession_rcg_fr.execute(select(T_CC.Id_CCName).where(T_CC.CCName ==  o_CCName)).first()[0]
            
            o_Id_CCName = DBSession_rcg_gb.execute(select(T_CC.Id_CCName).filter_by(CCName = o_CCName)).scalar_one()

            stmt = insert(T_CCR_Bonuses).values( Id_CCName =o_Id_CCName,
            SavePsychic = o_SavePsychic, SaveComaDeath = o_SaveComaDeath, SaveMagic = o_SaveMagic,
            SavePoison = o_SavePoison, SaveMindControl = o_SaveMindControl, SaveToxins = o_SaveToxins, 
            BonusTrust = o_BonusTrust, BonusCharm = o_BonusCharm, BonusHTHDamage = o_BonusHTHDamage, 
            BonusParry = o_BonusParry, BonusDodge = o_BonusDodge, BonusStrike = o_BonusStrike, 
            BonusPullPunch = o_BonusPullPunch, BonusRoll = o_BonusRoll, BonusInitiative = o_BonusInitiative, 
            AttacksMelee = o_AttacksMelee, Horror = o_Horror, IQ  = o_IQ ,  MA  = o_MA ,  ME  = o_ME  , 
            PS  = o_PS ,  PP  = o_PP ,  PE  = o_PE ,  PB  = o_PB ,  Spd  = o_Spd ,  SDC  = o_SDC , 
            MDC  = o_MDC ,  HP  = o_HP ,  ISP  = o_ISP ,  PPE  = o_PPE ,  CommBonus  = o_CommBonus ,
            DomBonus  = o_DomBonus ,  ElecBonus  = o_ElecBonus ,  EspBonus  = o_EspBonus ,  LangBonus  = o_LangBonus , 
            MechBonus  = o_MechBonus ,  MedBonus  = o_MedBonus ,  MilBonus  = o_MilBonus ,  PhyBonus  = o_PhyBonus ,
            PilotBonus  = o_PilotBonus ,  PRBonus  = o_PRBonus ,  RogueBonus  = o_RogueBonus ,  SciBonus  = o_SciBonus , 
            TechBonus  = o_TechBonus ,  WildBonus = o_WildBonus)
        try:
            DBSession_rcg_fr.execute(stmt)
        except  Exception as erreur:
            print("Erreur:" , erreur)
            DBSession_rcg_fr.rollback()
        else:
            DBSession_rcg_fr.commit()

        try:
            DBSession_rcg_gb.execute(stmt)
        except  Exception as erreur:
            print("Erreur:" , erreur)
            DBSession_rcg_gb.rollback()
        else:
            DBSession_rcg_gb.commit() 

    
def table_T_GroupeREF(sql_requete):            
    cur_BaseOrigine.execute(sql_requete)
    print("Alimentation des groupes")
    
           
            
def table_CCR_Knowledge(sql_requete):
    cur_BaseOrigine.execute(sql_requete)
    print("Charger CCR_Knowledge")

    resultat = cur_BaseOrigine.fetchall()  # fetchall() :  
    print("---")
    for _CCName , _LevelGained, _Knowledge, _Param1, _Param2, _Param3 , _Param4 , _Param5, _Param1Amount , _Param2Amount , _Param3Amount , _Param4Amount , _Param5Amount  in resultat:
          
        #base FR
        try: 
            o_Id_CCName = DBSession_rcg_fr.execute(select(T_CC.Id_CCName).filter_by(CCName = _CCName)).scalar_one()
       
        except  Exception as  NoResultFound: 
            print(f"T_CC inconnu : {_CCName}")
            stmt = insert(T_CC).values( CCName = _CCName  ) # ajout d d'un CC inconnu de la base CC
            o_Id_CCName = DBSession_rcg_fr.execute(select(T_CC.Id_CCName).filter_by(CCName = _CCName)).scalar_one()
        
        except  Exception as erreur:
            print("Erreur:" , erreur)
        # referecnes  Id_knowlegde 
        data_groupe_knowlegde = GroupeREF(None, _Knowledge, "Knowledge", None)
        o_Id_knowlegde = data_groupe_knowlegde.Id_GroupeREF_fr(None, _Knowledge, "Knowledge", None)
        

        stmt = insert(T_CCR_Bonuses).values( Id_CCName = o_Id_CCName, LevelGained = _LevelGained , Id_Groupe_Knowledge=o_Id_knowlegde ,
                                             Param1 = _Param1 , Param1Amount = _Param1Amount , 
                                             Param2 = _Param2 , Param2Amount = _Param2Amount ,  
                                             Param3 = _Param3 , Param3Amount = _Param3Amount , 
                                             Param4 = _Param4 , Param4Amount = _Param4Amount ,  
                                             Param5 = _Param5 , Param5Amount = _Param5Amount)
             
        try:
            DBSession_rcg_fr.execute(stmt)
        except  Exception as erreur:
            print("Erreur:" , erreur)
            DBSession_rcg_fr.rollback()
        else:
            DBSession_rcg_fr.commit() 
            
        #base gb
        try: 
            o_Id_CCName = DBSession_rcg_gb.execute(select(T_CC.Id_CCName).filter_by(CCName = _CCName)).scalar_one()
        except  Exception as  NoResultFound: 
            print(f"T_CC inconnu : {_CCName}")
            stmt = insert(T_CC).values( CCName = _CCName  ) # ajout d d'un CC inconnu de la base CC
            o_Id_CCName = DBSession_rcg_gb.execute(select(T_CC.Id_CCName).filter_by(CCName = _CCName)).scalar_one()
        except  Exception as erreur:
            print("Erreur:" , erreur)
        # referecnes  Id_knowlegde 
        data_groupe_knowlegde = GroupeREF(None, _Knowledge, "Knowledge", None)
        o_Id_knowlegde = data_groupe_knowlegde.Id_GroupeREF_gb()
        

        stmt = insert(T_CCR_Bonuses).values( Id_CCName = o_Id_CCName, LevelGained = _LevelGained , Id_Groupe_Knowledge=o_Id_knowlegde ,
                                             Param1 = _Param1 , Param1Amount = _Param1Amount , 
                                             Param2 = _Param2 , Param2Amount = _Param2Amount ,  
                                             Param3 = _Param3 , Param3Amount = _Param3Amount , 
                                             Param4 = _Param4 , Param4Amount = _Param4Amount ,  
                                             Param5 = _Param5 , Param5Amount = _Param5Amount)
             
        try:
            DBSession_rcg_gb.execute(stmt)
        except  Exception as erreur:
            print("Erreur:" , erreur)
            DBSession_rcg_gb.rollback()
        else:
            DBSession_rcg_gb.commit() 


def table_XX(sql_requete):
    cur_BaseOrigine.execute(sql_requete)
    print("Charger Table CCR_Bonuses")
    resultat = cur_BaseOrigine.fetchall()  # fetchall() :  
    for x in resultat :
        stmt = insert(T_CCR_Bonuses).values( Id_CCName =x )
        try:
            DBSession_rcg_fr.execute(stmt)
        except  Exception as erreur:
            print("Erreur:" , erreur)
            DBSession_rcg_fr.rollback()
        else:
            DBSession_rcg_fr.commit()
    
        try:
            DBSession_rcg_gb.execute(stmt)
        except  Exception as erreur:
            print("Erreur:" , erreur)
            DBSession_rcg_gb.rollback()
        else:
            DBSession_rcg_gb.commit()    
                        


if __name__ == '__main__':


    sql_Bionics_Base_Access = """SELECT `Category`, `ItemName`, `Cost`, `Cat`, `Location`, `Description` FROM `Bionics`; """
    sql_Bionics_Category_Base_Access = """ SELECT DISTINCT `Category` FROM `Bionics`;"""
    sql_Bionic_Weapon  =""" SELECT `ItemName`, `Damage`, `Effect`, `Payload`, ROF, `Range` FROM `Bionic_Weapon`;""" 
    
    sql_cc = """
    SELECT `CCName`, `CCType`, `ISPLevel`, `PPELevel`, `MDCLevel`, `MaxHP`, `MinHP`, `MaxSDC`,
    `MinSDC`, `MaxMDC`, `MinMDC`, `MaxPPE`, `MinPPE`, `MaxISP`, `MinISP`, `MaxIQ`, `MinIQ`,
    `MaxMa`, `MinMa`, `MaxMe`, `MinMe`, `MaxPs`, `MinPs`, `MaxPp`, `MinPp`, `MaxPe`, `MinPe`,
    `MaxPb`, `MinPb`, `MaxSpd`, `MinSpd`, `NoLang`, `NoWp`, `American`, `Dragonese`, `NoRSkills`,
    `NoSSkills`, `RequiredWP1`, `RequiredWP2`, `RequiredWP3`, `RequiredWP4`, `ReqSkillCat1`,
    `ReqSkillCat2`, `ReqSkillCat3`, `ReqSkillNum1`, `ReqSkillNum2`, `ReqSkillNum3`, `HTHBasic`,
    `HTHExpert`, `HTHMartialArts`, `HTHAssassin`, `NAwHTH`, `NAintHTH`, `AncientRq`, `ModernRq`,
    `PilotRq`, `AncientNo`, `ModernNo`, `PilotNo`, `SkillSelection`, `Description`, 
     `RSkillBonus`, `Credits`, `BMCredits`, `PowerType`, `Book`, `Cybernetics`, `Bionics`
     FROM CC;
    """
    
    sql_CCR_Progression = """
    SELECT `CCName`, `Level`, `NoRSkills`, `NoSSkills`, `NoWP`, `NoSpells`,
    `NoESpells`, `NoESpellsAir`, `NoESpellsFire`, `NoESpellsWater`, `NoESpellsEarth`,
    `NoPsionics`, `NoGenPsionics`, `NoPsiSensitive`, `NoPsiPhysical`, `NoPsiHealing`, 
    `NoPsiSuper`, `SpellLevels`, `MinLevel`, `NoSmpWeapon`, `NoMagWeapon`, `NoAnimal`, `NoMonster`, `NoPower`
    FROM `CCR_Progression`;
    """
    
    sql_CC_Abilities = """
        SELECT `CCName`, `Ability`
        FROM `CC_Abilities`;
        """
              
    sql_CCR_Bonuses = """
    SELECT `CCName`, `SavePsychic`, `SaveComaDeath`, `SaveMagic`, `SavePoison`, `SaveMindControl`, 
    `SaveToxins`, `BonusTrust`, `BonusCharm`, `BonusHTHDamage`, `BonusParry`, `BonusDodge`,
     `BonusStrike`, `BonusPullPunch`, `BonusRoll`, `BonusInitiative`, `AttacksMelee`, 
     `Horror`, IQ, MA, ME, PS, PP, PE, PB, `Spd`, SDC, MDC, HP, ISP, PPE, `CommBonus`, 
     `DomBonus`, `ElecBonus`, `EspBonus`, `LangBonus`, `MechBonus`, `MedBonus`, `MilBonus`,
      `PhyBonus`, `PilotBonus`, `PRBonus`, `RogueBonus`, `SciBonus`, `TechBonus`, `WildBonus`
        FROM `CCR Bonuses`;
    """        
    
    sql_CCR_Knowledge = """
    SELECT `CCName`, `LevelGained`, `Knowledge`, `Param1`, `Param2`, `Param3`, `Param4`, `Param5`,
        `Param1Amount` , `Param2Amount`, `Param3Amount`, `Param4Amount`, `Param5Amount`
      FROM `CC_Knowledge`;
    """

    sql_goupeCCR_Knowledge = """
    SELECT distinct  `Knowledge` FROM `CC_Knowledge`;
    """
                                       
    try :
 
        # initialisation Banse Français
        init_sqlalchemy_rcg_fr()

        # initialisation Banse Anglais       
        init_sqlalchemy_rcg_gb()
        
        connection_BaseOrigine = pyodbc.connect(BaseOrigine)  # Connexion a la base Access
        cur_BaseOrigine = connection_BaseOrigine.cursor()     # Curseur  a la base Access     

        table_Category(sql_Bionics_Category_Base_Access)
        table_bionic(sql_Bionics_Base_Access ) #construction
        table_Bionic_Weapon(sql_Bionic_Weapon) 
        table_CC(sql_cc)
        table_CCR_Progression(sql_CCR_Progression) 
        table_CC_Abilities(sql_CC_Abilities)
        table_CCR_Bonuses(sql_CCR_Bonuses) 
        
        cur_BaseOrigine.execute(sql_goupeCCR_Knowledge)
        print("Charger groupe table CCR_Knowledge")
        resultat = cur_BaseOrigine.fetchall()  # fetchall() :  
        for name, in resultat :
            data_groupe_knowlegde = GroupeREF(None, name, "Knowledge", None)
            data_groupe_knowlegde.update_fr()
            data_groupe_knowlegde.update_gb()

        table_CCR_Knowledge(sql_CCR_Knowledge)
        
        print("fin du traitement") 
        
    except  Exception as erreur:
        print("Erreur:" , erreur)
 
    finally:    
        pass
