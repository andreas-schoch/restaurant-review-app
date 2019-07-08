import React from 'react';
import ReactDOM from 'react-dom';
// import './css/index.css';
import App from './components/App';
import { Provider } from 'react-redux'
import {  BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { store } from './store'

import Home from './components/Home';


ReactDOM.render(
    <Provider store={store}>
        <Router>
            <Switch>
                <App>

                    <Route exact path='/' exact component={ Home } />
                </App>
            </Switch>
        </Router>
    </Provider>
, document.getElementById('root'));

