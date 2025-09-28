import React, { useState } from 'react';

const LandingPage = () => {
  const [professor, setProfessor] = useState('');
  const [crn, setCrn] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    
    // Validate CRN is exactly 6 digits
    if (!/^\d{6}$/.test(crn)) {
      setError('CRN must be exactly 6 digits');
      return;
    }
    
    setIsSubmitting(true);
    
    // TODO
    setTimeout(() => {
      console.log('Professor:', professor);
      console.log('CRN:', crn);
      setIsSubmitting(false);
    }, 500);
  };

  return (
    <div className="landing-container">
      <div className="floating-shapes">
        <div className="shape shape-1"></div>
        <div className="shape shape-2"></div>
        <div className="shape shape-3"></div>
        <div className="shape shape-4"></div>
      </div>
      
      <div className="content-wrapper">
        <div className="hero-section">
          <h1 className="hero-title">
            Course Compass
          </h1>
          <p className="hero-subtitle">
            Enter a professor and/or CRN.
          </p>
        </div>

        <div className="form-container">
          <form onSubmit={handleSubmit} className="registration-form">
            <div className="input-group">
              <label htmlFor="professor" className="input-label">
                Professor Name
              </label>
              <input
                type="text"
                id="professor"
                value={professor}
                onChange={(e) => setProfessor(e.target.value)}
                className="form-input"
                placeholder="Enter professor's name"
                required
              />
            </div>

            <div className="input-group">
              <label htmlFor="crn" className="input-label">
                CRN (Course Reference Number)
              </label>
              <input
                type="text"
                id="crn"
                value={crn}
                onChange={(e) => setCrn(e.target.value)}
                className="form-input"
                placeholder="Enter CRN"
                required
              />
            </div>

            {error && (
              <div className="error-message">
                <span className="error-icon">⚠️</span>
                {error}
              </div>
            )}

            <button
              type="submit"
              className={`submit-button ${isSubmitting ? 'submitting' : ''}`}
              disabled={isSubmitting}
            >
              {isSubmitting ? (
                <span className="loading-text">
                  <span className="spinner"></span>
                  Processing...
                </span>
              ) : (
                'Submit'
              )}
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default LandingPage;
