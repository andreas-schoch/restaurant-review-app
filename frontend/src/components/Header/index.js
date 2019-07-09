import React from 'react';
import {  Link } from 'react-router-dom';
import './index.scss';


const Header = (props) => {
    return (
        <header className='main-header'>
            <div className='main-header-logo'>Luna</div>
            <nav className='main-header-nav'>
                <Link to="/">Home</Link>
                <Link to="/">Search</Link>
                <Link to="/me">Profile</Link>
            </nav>

            <div className='main-header-btns'>
                <button>Temp</button>
                <button>Temp</button>
            {/* need to create a component that displays a logout button when logged in or
               signup and login buttons when logged out, all except logout could be anchors (Link) */}
            </div>
        </header>
    );
};

export default Header;