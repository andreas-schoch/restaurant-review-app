import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import { Provider } from 'react-redux'
import {  BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { store } from './store'

import App from './components/App';
//import Login from './components/Login'
import Home from './components/Home';
import UserProfile from './components/UserProfile';
import Login from './components/Login';
import Search from './components/Search';


ReactDOM.render(
    <Provider store={store}>
        <Router>
            <Switch>
                <App>
                    <Route  path='/' exact component={ Home } />
                    <Route  path='/login' exact component={ Login } />
                    <Route  path='/search' exact component={ Search } />
                    <Route  path='/restaurants'  component={ Login } />
                    <Route  path='/restaurants/:restaurant_id'  component={ Login } />
                    <Route  path='/me' component={ UserProfile } />
                </App>
            </Switch>
        </Router>
    </Provider>
, document.getElementById('root'));

