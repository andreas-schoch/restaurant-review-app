import React, { useState } from "react";
import { connect } from "react-redux";
import { loginAction } from "../../store/actions/loginAction";
import './index.scss';

function Login({ dispatch, history }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const login = async e => {
    e.preventDefault();
    const data = await dispatch(loginAction({ username, password }));
    if (data) history.push("/feed");
  };

  return (
    <form onSubmit={login}>
      <input
        type="text"
        value={username}
        placeholder="Your username"
        name="username"
        onChange={e => setUsername(e.target.value)}
      />

      <input
        type="password"
        value={password}
        placeholder="Your password"
        name="password"
        onChange={e => setPassword(e.target.value)}
      />
      <LoginButton>login</LoginButton>
    </form>
  );
}

export default connect()(Login);
