export default class Pokemon {
    name: string;
    sprite: string;
    shinySprite: string;
    hp: number;
    attack: number;
    defense: number;
    spAttack: number;
    spDefense: number;
    speed: number;

    constructor(name: string, sprite: string, shinySprite: string, hp:number, attack:number, defense:number, spAttack:number, spDefense:number, speed:number){
        this.name = name;
        this.sprite = sprite;
        this.shinySprite = shinySprite;
        this.hp = hp;
        this.attack = attack;
        this.defense = defense;
        this.spAttack = spAttack;
        this.spDefense = spDefense;
        this.speed = speed;
    }
}