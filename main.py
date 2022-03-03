def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(assets.image("""ammo"""), spacePlane, 200, 0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite2, otherSprite2):
    otherSprite2.destroy()
    scene.camera_shake(4, 500)
    info.change_life_by(-1)
    music.small_crash.play(69)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
    info.change_score_by(1)
    music.big_crash.play(66)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

bogey: Sprite = None
projectile: Sprite = None
spacePlane: Sprite = None
spacePlane = sprites.create(assets.image("""
    spacePlane
"""), SpriteKind.player)
controller.move_sprite(spacePlane, 200, 200)
spacePlane.set_stay_in_screen(True)
info.set_life(3)

def on_update_interval():
    global bogey
    bogey = sprites.create(assets.image("""
        bogey
    """), SpriteKind.enemy)
    bogey.set_velocity(-100, 0)
    bogey.set_position(160, randint(5, 115))
    bogey.set_flag(SpriteFlag.AUTO_DESTROY, False)
game.on_update_interval(500, on_update_interval)
