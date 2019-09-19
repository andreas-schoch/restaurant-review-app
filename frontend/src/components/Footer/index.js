import React from 'react';
import './index.scss';

 // TODO change path of icons for deployment
const Footer = (props) => {
    return (
        < footer className='main-footer'>
            <nav className='main-footer-nav'>
                <div className='main-footer-nav-left'>
                    <a href="#">About Us</a>
                    <a href="#">Press</a>
                    <a href="#">Blog</a>
                    <a href="#">iOS</a>
                    <a href="#">Android</a>
                </div>
                <div className='main-footer-nav-right'>
                    <a href='#'><img src="/assets/svg/facebook.svg" alt="icon" /></a>
                    <a href='#'><img src="/assets/svg/twitter.svg" alt="icon" /></a>
                    <a href='#'><img src="/assets/svg/googleplus.svg" alt="icon" /></a>
                    <a href='#'><img src="/assets/svg/instagram.svg" alt="icon" /></a>

                </div>
            </nav>
            <div className='main-footer-nav-copyright'>
                <span>&copy; Copyright Luna 2019</span>
            </div>


        </footer>
    );
};

export default Footer;