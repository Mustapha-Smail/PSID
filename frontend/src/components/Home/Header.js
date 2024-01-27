import React from 'react'
import { useNavigate } from 'react-router-dom'
import './Header.css'

const Header = () => {
    const navigate = useNavigate()

    return (
        <div className="st__header section__padding" id="home">
            <div className="st__header-content">
                <h1 className="gradient__text">
                    Découvrez l'Europe à travers la donnée
                </h1>
                <p>
                    Explorez les tendances culinaires et les palais diversifiés avec notre tableau de bord interactif sur les restaurants européens.
                </p>

                <div className="st__header-content__input">
                    <button type="button" onClick={() => navigate('/dashboard')}>C'est parti!</button>
                </div>

            </div>

            <div className="st__header-image">
                <img src="/logo_transparent.png" alt="upn" /> <br></br>
            </div>
        </div>
    )
};

export default Header;