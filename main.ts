controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    projectile = sprites.createProjectileFromSprite(assets.image`ammo`, spacePlane, 200, 0)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap(sprite2: Sprite, otherSprite2: Sprite) {
    otherSprite2.destroy()
    scene.cameraShake(4, 500)
    info.changeLifeBy(-1)
    music.smallCrash.play(69)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function on_on_overlap2(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy()
    info.changeScoreBy(1)
    music.bigCrash.play(66)
})
let bogey : Sprite = null
let projectile : Sprite = null
let spacePlane : Sprite = null
spacePlane = sprites.create(assets.image`
    spacePlane
`, SpriteKind.Player)
controller.moveSprite(spacePlane, 200, 200)
spacePlane.setStayInScreen(true)
info.setLife(3)
game.onUpdateInterval(500, function on_update_interval() {
    
    bogey = sprites.create(assets.image`
        bogey
    `, SpriteKind.Enemy)
    bogey.setVelocity(-100, 0)
    bogey.setPosition(160, randint(5, 115))
    bogey.setFlag(SpriteFlag.AutoDestroy, false)
})
