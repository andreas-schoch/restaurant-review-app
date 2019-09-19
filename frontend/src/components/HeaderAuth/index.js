import React from 'react';
import {  Link, withRouter } from 'react-router-dom';
import './index.scss';
import { Button } from '../../styled'

const HeaderAuth = (props) => {
    const token = localStorage.getItem('token');
    let authenticated = !!token; // TODO check if token valid and set it accordingly

    const logoutHandler = (e) => { // TODO TEMPORARY refactor to use logout action in the future
        console.log(props);
        localStorage.clear();
        props.history.push('/');
    }

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

export default withRouter(HeaderAuth);