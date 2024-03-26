import { useEffect } from 'react';
import './PokeCard.css'
import Pokemon from './Pokemon';

export default function PokeCard({name, sprite, shinySprite, hp, attack, defense, spAttack, spDefense, speed}: Pokemon){

    return(
        <button className="card">
            <div className='sprite'>
                <img src={sprite} alt="SearchedSprite"/>
            </div>
            <div className='info'>
                <div><p>{name}</p></div>
                <div id='hpBar'>HP: {hp}/{hp}</div>
            </div>
        </button>
    );
}

