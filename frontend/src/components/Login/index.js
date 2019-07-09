import React, { useState } from 'react';
import { connect } from 'react-redux';

import { loginAction } from '../../store/actions/loginAction';

function Login(props) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const login = async e => {
    e.preventDefault();
    const tokens = await props.dispatch(loginAction(username, password));
    if (tokens.access) props.history.push('/home');
  };

  return (
    <form onSubmit={ login }>
      <input
        type="text" value={ username } placeholder="Username" name="username"
        onChange={ (e) => setUsername(e.target.value) }
      />

      <input
        type="password" value={ password } placeholder="Password" name="password"
        onChange={ (e) => setPassword(e.target.value) }
      />
      <button>Login</button>
    </form>
  );
}

export default connect()(Login);
