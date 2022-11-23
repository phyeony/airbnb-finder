import {
  Button, 
  FormLabel,
  FormControl,
  FormGroup,
  FormControlLabel,
  FormHelperText,
  Checkbox,
  Stack
} from '@mui/material';

import {useState} from 'react';

function App() {
  const [state, setState] = useState({
    gilad: true,
    jason: false,
    antoine: false,
  });

  const handleChange = (event) => {
    setState({
      ...state,
      [event.target.name]: event.target.checked,
    });
  };

  const { gilad, jason, antoine } = state;
  const error = [gilad, jason, antoine].filter((v) => v).length !== 2;

  const handleSubmit = () => {
    const data = ['sdf']
    console.log("submitted")
    fetch("http://localhost:8000/airbnb_list")
      .then((res) => console.log(res))
      .catch((e) => console.error(e))
  }
        /* Airbnb 
      1. Room type - select
      2. Price range

      1. Attraction 
      2. Food
      3. Transportation */

  return (
      <Stack>
      <h3>Airbnb Finder</h3>
      
      <FormControl sx={{ m: 3 }} component="fieldset" variant="standard">
        <FormLabel component="legend">Assign responsibility</FormLabel>
        <FormGroup>
          <FormControlLabel
            control={
              <Checkbox checked={gilad} onChange={handleChange} name="gilad" />
            }
            label="Gilad Gray"
          />
          <FormControlLabel
            control={
              <Checkbox checked={jason} onChange={handleChange} name="jason" />
            }
            label="Jason Killian"
          />
          <FormControlLabel
            control={
              <Checkbox checked={antoine} onChange={handleChange} name="antoine" />
            }
            label="Antoine Llorca"
          />
        </FormGroup>
        <FormHelperText>Be careful</FormHelperText>
      </FormControl>
      <Button variant="contained" onClick={handleSubmit}>Hello World</Button>


</Stack>
  );
}

export default App;

