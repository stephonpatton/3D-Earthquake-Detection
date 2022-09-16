import './App.css';
import Globe from 'react-globe.gl';
import React from "react"
import {useEffect, useRef} from "react";

function App() {
  const { useEffect, useRef } = React;
  const World = () => {
    const globeEl = useRef();
    useEffect(() => {

      const globe = globeEl.current;

      // Auto-rotate
      globe.controls().autoRotate = true;
      globe.controls().autoRotateSpeed = 0.50;
    }, []);

    return <Globe
      ref={globeEl}
      animateIn={false}
      globeImageUrl="//unpkg.com/three-globe/example/img/earth-blue-marble.jpg"
      bumpImageUrl="//unpkg.com/three-globe/example/img/earth-topology.png"
    />;

  };




  return (
      <World />
  )


}

export default App;
