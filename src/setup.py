'''
Documentation cx_freeze: http://cx-freeze.readthedocs.org/en/latest/
To generate, type:
python setup.py build
'''

from cx_Freeze import setup,Executable

'''
The whole data folder should be copied into directory with the exe
includefiles = [
                'data/barke1_385x385.png',
                'data/barke2_448x448.png',
                'data/bg_pfeile.png',
                'data/char_attack1_effect.png',
                'data/char.png',
                'data/characters.png',
                'data/collectibles.png',
                'data/curse_green_effect.png',
                'data/curse_pink_effect.png',
                'data/enemy_green_1.png',
                'data/enemy_pink_1.png',
                'data/enemy_pink_boss.png',
                'data/field.png',
                'data/for_tests_only.tmx',
                'data/heal_potion_s.png',
                'data/heal_potion_l.png',
                'data/heal_potion_m.png',
                'data/hp.png',
                'data/orb.png',
                'data/pink_proj',
                'data/portal.png',
                'data/projectile_fly_green.png',
                'data/projectile_fly_orange.png',
                'data/simple_projectile_light_circle.png',
                'data/skill_pot.png',
                'data/sprite_felsentiles2d_mitBG.png',
                'data/sprite_felsentiles2e_mitBG.png',
                'data/sprite_felsentiles2f_mitBG.png',
                'data/tentakel.png'
                'data/tentakel2.png'
                'data/test.tmx',
                'data/test2.tmx',
                'data/test3.tmx',
                'data/tileset_green_01.png',
                'data/tileset_neutral_01.png',
                'data/tileset_pink_01.png'
                ]
'''

build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}#, 'include_files':includefiles}

setup(
      name = 'Chaos Projectile',
      version = '0.4',
      description = 'Chaos Projectile - Run n Gun meets RPG',
      #author = 'Anna Dorokhova',
      options = {"build_exe": build_exe_options},
      executables = [Executable(script="game.py", base="Win32GUI", targetName="Chaos-Projectile.exe")]
      )
