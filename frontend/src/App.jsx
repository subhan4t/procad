// frontend/src/App.js
import React, { useState } from 'react';
import Navbar from './components/Navbar';
import LoginDialog from './components/LoginDialog';
import { AuthContext } from './context/AuthContext';

function App() {
  // Auth state
  const [auth, setAuth] = useState({
    loggedIn: false,
    user: null,
    isAdmin: false,
  });

  // Login dialog open state
  const [loginOpen, setLoginOpen] = useState(false);

  // Open login dialog handler
  const handleLoginOpen = () => setLoginOpen(true);

  // Close login dialog handler
  const handleLoginClose = () => setLoginOpen(false);

  // Optional: Handle settings click
  const handleSettingsClick = () => {
    alert('Settings feature coming soon!');
  };

  return (
    <AuthContext.Provider value={{ auth, setAuth }}>
      <Navbar onLoginClick={handleLoginOpen} onSettingsClick={handleSettingsClick} />
      <LoginDialog open={loginOpen} onClose={handleLoginClose} />

      <main style={{ padding: '1rem' }}>
        {auth.loggedIn ? (
          <div>
            <h2>Welcome, {auth.user.name}!</h2>
            <p>{auth.isAdmin ? 'You have admin access.' : 'You are logged in as a user.'}</p>
          </div>
        ) : (
          <h2>Please login to continue.</h2>
        )}
      </main>
    </AuthContext.Provider>
  );
}

export default App;
