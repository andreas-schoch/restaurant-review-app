import React from 'react';
import './index.scss';


const Footer = (props) => {
    return (
        < footer className='main-footer'>
            <nav className='main-footer-nav'>
                <div>
                    <a href='#'>About Us</a>
                    <a href='#'>Press</a>
                    <a href='#'>Blog</a>
                    <a href='#'>iOS</a>
                    <a href='#'>Android</a>
                </div>
                <div>
                    <a href='#'>icon</a>
                    <a href='#'>icon</a>
                    <a href='#'>icon</a>
                    <a href='#'>icon</a>
                </div>
            </nav>
            <div className='main-footer-nav-copyright'>
                <span>&copy; Copyright Luna 2019</span>
            </div>


        </footer>
    );
};

export default Footer;