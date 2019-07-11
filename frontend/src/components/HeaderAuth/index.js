import React from 'react';
import {  Link } from 'react-router-dom';
import './index.scss';
import { Button } from '../../styled'

const HeaderAuth = (props) => {
    let authenticated = false; // TODO check if token valid and set it accordingly

    const logoutHandler = (e) => console.log("logout");

    const chooseVisibleActions = () => {
        if (authenticated) {
            return (<Button onClick={logoutHandler}>Logout</Button>);
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