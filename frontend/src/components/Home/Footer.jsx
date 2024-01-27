import { Link } from '@mui/material'
import React from 'react'
import './footer.css'

const Footer = () => (
  <div className='st__footer'>
    <div className='st__footer-links'>
      <div className='st__footer-links_logo'>
        {/* <h1> */}
        <img
          src='/logo_transparent.png'
          alt=''
          srcset='/logo_transparent.png'
          style={{ width: '120px' }}
        />
        {/* </h1> */}
        <p>
          {/* Make food data worth */}
        </p>
      </div>
      <div className='st__footer-links_div'>
        <h4>Liens</h4>
        <Link
          href='/'
          style={{ textDecoration: 'none', color: 'black' }}
        >
          <p>Accueil</p>
        </Link>
        <Link
          href='/dashboard'
          style={{ textDecoration: 'none', color: 'black' }}
        >
          <p>Dashboard</p>
        </Link>
        <Link
          href='/details'
          style={{ textDecoration: 'none', color: 'black' }}
        >
          <p>Details</p>
        </Link>
      </div>
      <div className='st__footer-links_div'>
        <h4>myRestaurant</h4>
        <Link
          href='#'
          style={{ textDecoration: 'none', color: 'black' }}
        >
          <p>Code source</p>
        </Link>
        <Link
          href='#'
          style={{ textDecoration: 'none', color: 'black' }}
        >
          <p>A propos de nous</p>
        </Link>
      </div>
    </div>

    <div className='st__footer-copyright'>
      <p>@{new Date().getFullYear()} myRestaurant. All rights reserved.</p>
    </div>
  </div>
)

export default Footer
