import React from 'react';
import {  Link } from 'react-router-dom';
import './index.scss';
import HeaderAuth from "../HeaderAuth";


const Header = (props) => {
    return (
        <header className='main-header'>
            <div className='main-header-logo'><img src="./assets/svg/logo.svg" alt="" /></div>
            <nav className='main-header-nav'>
                <Link to="/">Home</Link>
                <Link to="/search">Search</Link>
                <Link to="/me">Profile</Link>
            </nav>

            <HeaderAuth />
        </header>
    );
};

export default Header;