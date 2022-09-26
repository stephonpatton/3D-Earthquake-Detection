import './App.css';
import Globe from 'react-globe.gl';
import React from "react"
import {useEffect, useRef} from "react";

function App() {
  const sample = [1,2,3,4,5]
  const { useEffect, useRef, useState} = React;
  const World = () => {
    const globeEl = useRef();
    const [equakes, setEquakes] = useState([]);

    useEffect(() => {
      // load data
      fetch('//earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.geojson').then(res => res.json())
        .then(({ features }) => setEquakes(features));
    }, []);


    useEffect(() => {

      const globe = globeEl.current;


      // Auto-rotate
      globe.controls().autoRotate = true;
      globe.controls().autoRotateSpeed = 0.50;
    }, []);

    // const myGlobe = Globe()
    //     .globeImageUrl('//unpkg.com/three-globe/example/img/earth-blue-marble.jpg')
    //     // .hexBinPointLat(34.1653333)
    //     // .hexBinPointLng(-80.7085)
    // return myGlobe
    return <Globe
      ref={globeEl}
      animateIn={false}
      globeImageUrl="//unpkg.com/three-globe/example/img/earth-blue-marble.jpg"
      bumpImageUrl="//unpkg.com/three-globe/example/img/earth-topology.png"
      hexBinPointsData={equakes}
      hexBinPointLat={d => d.geometry.coordinates[1]}
      hexBinPointLng={d => d.geometry.coordinates[0]}
      hexBinPointWeight={d => d.properties.mag}
      hexAltitude={({ sumWeight }) => sumWeight * 0.0025}
      hexTopColor={700}
      hexSideColor={200}
      hexLabel={d => `
        <b>${d.points.length}</b> earthquakes in the past month:<ul><li>
          ${d.points.slice().sort((a, b) => b.properties.mag - a.properties.mag).map(d => d.properties.title).join('</li><li>')}
        </li></ul>
      `}
    />;
  };

  // TODO: Add sample point data to Globe
  // https://github.com/vasturiano/globe.gl/blob/master/example/earthquakes/index.html
  // https://globe.gl/#points-layer

  // TODO: Get data from database or parse differently on the globe
  // TODO: Change earthquake stat graphic from line to something cool (ripple, etc)

  return (
      <World />
  )


}

export default App;
