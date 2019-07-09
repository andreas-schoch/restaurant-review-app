import React from 'react';
import Header from '../Header'
import Footer from '../Footer'

const App = (props) => {
    return (
        <>
            <Header className='main-header'/>
            { props.children }
            <Footer className={'main-footer'}/>
        </>
    );
};

export default App;