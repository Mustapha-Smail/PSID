import { Grid, Link } from '@mui/material'
import React from 'react'
import CardGraph from '../CardGraph/CardGraph'
import Feature from './Feature'
import Graphes from './Graphes'
import './Main.css'

const Main = () => (
  <div
    className='st__whatSignTalk section__margin'
    id='fonctionnalites'
  >
    <div className='st__whatSignTalk-feature'>
      <Feature
        title="À la table de l'Europe"
        text="L'Europe se présente comme un véritable carrefour de cultures gastronomiques, où chaque nation offre un bouquet unique de saveurs et d'expériences culinaires. Ce rapport propose d'explorer comment la tradition, l'adaptation et la recherche de qualité définissent la gastronomie européenne. L'adaptabilité des restaurateurs face aux changements des régimes alimentaires en Europe démontre leur capacité à vouloir évoluer tout en préservant les héritages culinaire propre à leur nation."
      />
    </div>
    <div className='st__whatSignTalk-heading'>
      <h1 className='gradient__text'>Le Guide des Saveurs en Europe</h1>
      <Link
        href='/dashboard'
        style={{ textDecoration: 'none', color: 'black' }}
      >
        <p>En savoir plus</p>
      </Link>
    </div>
    <div className='st__whatSignTalk-container'>
      <Graphes />
    </div>
    <div className='st__whatSignTalk-feature'>
      <Feature
        title='Synthèse'
        text="Dans l'ensemble, l'histoire racontée par ces graphiques est celle d'une Europe où la tradition culinaire tend vers l'adaptation, où la diversité est célébrée et où la qualité est recherchée dans toutes les gammes de prix. C'est un continent où manger et découvrir des cultures est plus qu'une nécessité et qu'on pourrait assimiler à une aventure. "
      />
    </div>
  </div>
)

export default Main
