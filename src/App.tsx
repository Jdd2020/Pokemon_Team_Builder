import React, { ReactElement, useEffect, useState } from 'react';
import Pokemon from './Pokemon';
import './App.css';
//import { updateQualifiedName } from 'typescript';
import PokeCard from './PokeCard';

function App() {
  const [search, updateSearch] = useState("");
  const [pokeResp, updateInfo] = useState(new Pokemon("", "", "", 0, 0, 0, 0, 0, 0));
  const [errorResp, setError] = useState(false);
  const [team, updateTeam] = useState<Pokemon[]>([]);



  const switchTeam = ( i : number) => {
    updateInfo(team[i]);
  }

  const pokeTeam = team.map( (poke, index) => 
    {
      return (
        <li key={index} onClick={() => switchTeam(index)}>
          <PokeCard {...poke}/>
        </li>
      )
    }
  );

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();

    console.log(search);

    fetch('https://pokeapi.co/api/v2/pokemon/' + search)
    .then((response) => response.json())
    .then((result) => {
      console.log(result);
      console.log(result['name']);
      let pokeSearch = new Pokemon(
        result['name'],
        result['sprites']['front_default'],
        result['sprites']['front_shiny'],
        result['stats'][0]['base_stat'],
        result['stats'][1]['base_stat'],
        result['stats'][2]['base_stat'],
        result['stats'][3]['base_stat'],
        result['stats'][4]['base_stat'],
        result['stats'][5]['base_stat'],
      );
      updateInfo(pokeSearch);
      setError(false);
    },
    (error) => {
      setError(true);
      //console.log(error);
    });
  }

  const handleNewTeam = () => {
    if(team.length < 6) {
      let newTeam : Pokemon[] = team.slice();
      newTeam.push(pokeResp);
      updateTeam(newTeam);
    }
  }

  useEffect(() => {
    fetch('https://pokeapi.co/api/v2/pokemon/squirtle')
    .then((response) => response.json())
    .then((result) => {
      let pokeSearch = new Pokemon(
        result['name'],
        result['sprites']['front_default'],
        result['sprites']['front_shiny'],
        result['stats'][0]['base_stat'],
        result['stats'][1]['base_stat'],
        result['stats'][2]['base_stat'],
        result['stats'][3]['base_stat'],
        result['stats'][4]['base_stat'],
        result['stats'][5]['base_stat'],
      );
      updateInfo(pokeSearch);
    });
  }, []);

  return (

    <div className="App">
      <div className="userForm">
        <form onSubmit={handleSearch}>
          <h2>Enter a Pokemon!</h2>
          <input 
            type='text'
            value={search}
            onChange={(e) => updateSearch(e.target.value)}
          />
          <button>Submit</button>
          <h3>{errorResp && "Not a Pokemon!"}</h3>
        </form>
        <button onClick={handleNewTeam} id='addPoke'>Add Pokemon</button>
      </div>
      <div className='infoScreen'>
        <div className='team'>
          <h1>Team</h1>
          <ul className='teamList'>
            {pokeTeam}
          </ul>
        </div>
        <PokemonObj {...pokeResp}/>
      </div>
    </div>
  );
}



function PokemonObj({name, sprite, shinySprite, hp, attack, defense, spAttack, spDefense, speed}: Pokemon){

  const [useSprite, updateSprite] = useState(sprite as string);
  const [buttonText, updateButton] = useState('Make it shiny!');
  const [isShiny, setShiny] = useState(false);

  function switchSprite(){
    if(isShiny){
      updateSprite(sprite);
      updateButton('Make it shiny!');
      setShiny(false)
    }
    else{
      updateSprite(shinySprite);
      updateButton('No! Not like that!');
      setShiny(true);
    }
    return
  }

  useEffect(() => {
    updateSprite(sprite);
  }, [sprite])

  return(
    <div className='pokemon'>
      <div className='title'>
        <h1>{name}</h1>
        <img src={useSprite} alt=''/>
        <button onClick={switchSprite}>{buttonText}</button>
      </div>

      <div className='baseStats'>
      <h2>Base Stats</h2>
        <div className='hp'>
          <p>HP: {hp}</p>
        </div>
        <div className='attack'>
          <p>ATK: {attack}</p>
        </div>
        <div className='defense'>
          <p>DEF: {defense}</p>
        </div>
        <div className='spAttack'>
          <p>spATK: {spAttack}</p>
        </div>
        <div className='spDefense'>
          <p>spDEF: {spDefense}</p>
        </div>
        <div className='speed'>
          <p>SPD: {speed}</p>
        </div>
      </div>
    </div>
  )
}

export default App;
