import React, { useEffect } from 'react';
import { connect } from 'react-redux';

export default WrappedComponent => {
  function AuthComponent(props) {

    const { tokens, history } = props;

    const userRedirect = () => {
      if (!tokens.access) history.push('/login');
    };

    useEffect(() => {
      userRedirect()
    });

    return <WrappedComponent { ...props }/>
  }

  const mapStateToProps = (state) => ({ auth: state.loginReducer.authenticated });

  return connect(mapStateToProps)(AuthComponent);
}
