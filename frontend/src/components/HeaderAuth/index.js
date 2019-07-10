import React from 'react';
import {  Link } from 'react-router-dom';
import './index.scss';


const HeaderAuth = (props) => {
    let authenticated = false;

    const logoutHandler = (e) => console.log("logout");

    const chooseVisibleActions = () => {
        if (authenticated) {
            return (<button onClick={logoutHandler}>Logout</button>);
        } else {
            return (
                <>
                    <Link to='/register'>Signup</Link>
                    <Link to='/login'>Login</Link>
                </>
                )
            }
        };

    return (<div className='main-header-auth'>{ chooseVisibleActions() }</div>);
};

export default HeaderAuth;