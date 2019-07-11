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
import { refreshAction } from "./store/actions/loginAction";
import jwtDecode from "jwt-decode";
import { login } from "./store/actions/loginAction";
import AuthComponent from "./HOC";
import SearchRestaurants from "./components/SearchRestaurants";
import SearchComments from "./components/SearchComments";
import SearchUsers from "./components/SearchUsers";
import SearchControls from "./components/SearchControls";


const token = localStorage.getItem("token");
if (token) {
  store.dispatch(login(token));
}

ReactDOM.render(
    <Provider store={store}>
        <Router>
            <Switch>
                <App>
                    <Route  path='/' exact component={ Home } />
                    <Route  path='/login' exact component={ Login } />
                    <Route  path='/search' component={ SearchControls } />
                    <Route  path='/me' component={ UserProfile } />
                </App>
            </Switch>
        </Router>
    </Provider>
, document.getElementById('root'));

export function checker() {
    try {
      let decoded = jwtDecode(token);
      let dateNow = new Date();
      return decoded.exp < dateNow.getTime();
    } catch (error) {
      console.log(error);
    }
  }

  function Redirecter(match) {
    console.log(checker());
    if (checker()) {
      return (
        <div>
          <Route component={AuthComponent(Home)} />
          <Route exact path={match.path} />
        </div>
      );
    } else {
      console.log("!token");
      return refreshAction(token);
    }
  }

