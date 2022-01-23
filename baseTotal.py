# coding: utf-8  
 
from  Liste_des_Tables import *
 
import pyodbc 
from AccessDB import Liste_des_Tables

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
        Liste_des_Tables.init_sqlalchemy_rcg_fr()

        # initialisation Banse Anglais       
        Liste_des_Tables.init_sqlalchemy_rcg_gb()
        
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
