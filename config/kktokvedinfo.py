
import time
from config.orm import Orm
# BASE_DIR = Path('C:/Users/kuroe/Desktop/projects/')
# name = BASE_DIR.joinpath('3801622.xlsx')
def kktokvedinfo():
    orm_=Orm()
    what_with_kkt = orm_.randomQuery("""
select `a`.`Date` AS `Dater`,`t1`.`midpr` AS `midpr`,`t1_1`.`potreb` AS `potreb`,`t2`.`lekarstvo` AS `lekarstvo`,`t2_1`.`price_lekarstvo` AS `price_lekarstvo`,
    `t3`.`kktab` AS `kktab`,`t4`.`toplivo` AS `toplivo`,`t4_1`.`potreblenietoplivo` AS `potreblenietoplivo`,`t5`.`shir` AS `shir`,`t5_1`.`Shirpotreb` AS `Shirpotreb`,
    `t8`.`Viruzka_MSP` AS `Viruzka_MSP`,`t9`.`Viruzka_NP` AS `Viruzka_NP`
    from (((((((((((((select (curdate() - interval (((`a`.`a` + (10 * `b`.`a`)) + (100 * `c`.`a`)) + (1000 * `d`.`a`)) day) AS `Date` 
    from (((((select 0 AS `a`) union all select 1 AS `1` union all select 2 AS `2` union all select 3 AS `3` union all select 4 AS `4` union all select 5 AS `5`
    union all select 6 AS `6` union all select 7 AS `7` union all select 8 AS `8` union all select 9 AS `9`) `a` join (select 0 AS `a` union all select 1 AS `1`
    union all select 2 AS `2` union all select 3 AS `3` union all select 4 AS `4` union all select 5 AS `5` union all select 6 AS `6` union all select 7 AS `7` 
    union all select 8 AS `8` union all select 9 AS `9`) `b`) join (select 0 AS `a` union all select 1 AS `1` union all select 2 AS `2` union all select 3 AS `3` 
    union all select 4 AS `4` union all select 5 AS `5` union all select 6 AS `6` union all select 7 AS `7` union all select 8 AS `8` union all select 9 AS `9`) `c`) 
    join (select 0 AS `a` union all select 1 AS `1` union all select 2 AS `2` union all select 3 AS `3` union all select 4 AS `4` union all select 5 AS `5` 
    union all select 6 AS `6` union all select 7 AS `7` union all select 8 AS `8` union all select 9 AS `9`) `d`))) `a`
    left join (select `prices`.`mid_price`.`datelikedale` AS `a`,1 AS `midpr` from `prices`.`mid_price` group by `prices`.`mid_price`.`datelikedale`) 
    `t1` on((`a`.`Date` = `t1`.`a`))) left join (select `prices`.`potreblenie`.`datelikedale` AS `a`,1 AS `potreb` from `prices`.`potreblenie` group by
    `prices`.`potreblenie`.`datelikedale`) `t1_1` on((`a`.`Date` = `t1_1`.`a`))) left join (select `prices`.`potreblenie_lekarstvo`.`datelikedale` AS `a`,1
    AS `lekarstvo` from `prices`.`potreblenie_lekarstvo` group by `prices`.`potreblenie_lekarstvo`.`datelikedale`) `t2` on((`a`.`Date` = `t2`.`a`))) left join 
    (select `prices`.`mid_price_lekarstvo`.`datelikedale` AS `a`,1 AS `price_lekarstvo` from `prices`.`mid_price_lekarstvo` 
    group by `prices`.`mid_price_lekarstvo`.`datelikedale`) `t2_1` on((`a`.`Date` = `t2_1`.`a`))) 
    left join (select `prices`.`kkt`.`datelikedale` AS `a`,1 AS `kktab` from `prices`.`kkt` 
    group by `prices`.`kkt`.`datelikedale`) `t3` on((`a`.`Date` = `t3`.`a`))) 
    left join (select `prices`.`mid_price_toplivo`.`datelikedale` AS `a`,1 AS `toplivo` from `prices`.`mid_price_toplivo` group by `prices`.`mid_price_toplivo`.`datelikedale`)
    `t4` on((`a`.`Date` = `t4`.`a`))) left join (select `prices`.`potreblenie_toplivo`.`datelikedale` AS `a`,1 AS `potreblenietoplivo` from `prices`.`potreblenie_toplivo`
    group by `prices`.`potreblenie_toplivo`.`datelikedale`) `t4_1` on((`a`.`Date` = `t4_1`.`a`))) 
    left join (select `prices`.`mid_price_schir`.`datelikedale` AS `a`,1 AS `shir` from `prices`.`mid_price_schir` group by `prices`.`mid_price_schir`.`datelikedale`)
    `t5` on((`a`.`Date` = `t5`.`a`))) left join (select `prices`.`potreblenie_schir`.`datelikedale` AS `a`,1 AS `Shirpotreb` from `prices`.`potreblenie_schir`
    group by `prices`.`potreblenie_schir`.`datelikedale`) `t5_1` on((`a`.`Date` = `t5_1`.`a`))) 
    
    left join (select `OKVED`.`Viruzka_MSP`.`datelikedale` AS `a`,1 AS `Viruzka_MSP` from `OKVED`.`Viruzka_MSP` group by `OKVED`.`Viruzka_MSP`.`datelikedale`)
    `t8` on((`a`.`Date` = `t8`.`a`))) left join (select `OKVED`.`Viruzka_NP`.`datelikedale` AS `a`,1 AS `Viruzka_NP` from `OKVED`.`Viruzka_NP`
    group by `OKVED`.`Viruzka_NP`.`datelikedale`) `t9` on((`a`.`Date` = `t9`.`a`))) 
   
	
    
    where ((`a`.`Date` >= '2017-01-01') and (`a`.`Date` <= (curdate() - 1))) 
    group by `a`.`Date`,`t1`.`midpr`,`t1_1`.`potreb`,`t2`.`lekarstvo`,`t2_1`.`price_lekarstvo`,`t3`.`kktab`,`t4`.`toplivo`,
    `t4_1`.`potreblenietoplivo`,`t5`.`shir`,`t5_1`.`Shirpotreb`,`t8`.`Viruzka_MSP`,
    `t9`.`Viruzka_NP` ORDER BY Dater DESC LIMIT 7""",1)
    tablesprav=['mid_price', 'potreblenie', 'potreblenie_lekarstvo','price_lekarstvo', 'kkt', 'mid_price_toplivo','potreblenie_toplivo','mid_price_shir','potreblenie_schir', 'Viruzka_MSP', 'Viruzka_NP']
    flag=0
    outstring = ''
    for i in range(len(what_with_kkt)):
        outstring= outstring + '<b>Не залито</b> ' + str(what_with_kkt[i][0]) + ': '
        for j in range(1,len(what_with_kkt[i])):
            if what_with_kkt[i][j] is None:
                outstring= outstring  + tablesprav[j-1]+ ', '
        if outstring[-2:]==": ":
            outstring = outstring[:-30] + "<b>Залито </b>" + str(what_with_kkt[i][0])+': '
            flag+=1
        outstring= outstring[:-2] + "; <br>"
    if flag<7:
        flag=0
    else:
        outstring="<b>ККТ и ОКВЭД на месте</b>"
    orm_.connclose()
    return (outstring, flag)
        


