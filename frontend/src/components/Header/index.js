import React from 'react';
import {  Link, withRouter } from 'react-router-dom';
import './index.scss';
import HeaderAuth from "../HeaderAuth";


const Header = (props) => {
    // find out which Link is active (for the orange underline)
    const getActiveTab =  () => {
        const p = props.location.pathname;
        if (p === "/") { return 1; }
        if (p.includes("search")) { return 2; }
        if (p.includes("me")) { return 3; }
        return 1;
    }
    let activeTab = getActiveTab();
    return (
        <header className='main-header'>
            <div className='main-header-logo'>Luna</div>
            <nav className='main-header-nav'>
                <Link className={activeTab === 1 ? 'nav-active' : ''} to="/">Home</Link>
                <Link className={activeTab === 2 ? 'nav-active' : ''} to="/search">Search</Link>
                <Link className={activeTab === 3 ? 'nav-active' : ''} to="/me">Profile</Link>
            </nav>

            <HeaderAuth />
        </header>
    );
};

export default withRouter(Header);