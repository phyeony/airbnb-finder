import {
  Button, 
  FormLabel,
  FormControl,
  FormGroup,
  FormControlLabel,
  Checkbox,
  Stack,
  Card,
  CardHeader,
  Divider,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Grid,
  Box,
  TextField
} from '@mui/material';

import {useState} from 'react';

function not(a, b) {
  return a.filter((value) => b.indexOf(value) === -1);
}

function intersection(a, b) {
  return a.filter((value) => b.indexOf(value) !== -1);
}

function union(a, b) {
  return [...a, ...not(b, a)];
}

function App() {
  const [state, setState] = useState({
    entire: false,
    pv: false,
    shared: false,
  });

  const handleChange = (event) => {
    setState({
      ...state,
      [event.target.name]: event.target.checked,
    });
  };

  const { entire, pv, shared } = state;
  const error = [entire, pv, shared].filter((v) => v).length !== 2;

  const handleSubmit = () => {
    const data = ['sdf']
    console.log("submitted")
    fetch("http://localhost:8000/airbnb_list") // TODO: 
      .then((res) => console.log(res))
      .catch((e) => console.error(e))
  }

  const [name, setName] = useState(0);
  const handleTextChange = (event) => {
    setName(event.target.value);
  };

  const [checked, setChecked] = useState([]);
  const [left, setLeft] = useState(['Food','Attraction','Public Transporation']);
  const [right, setRight] = useState([]);

  const leftChecked = intersection(checked, left);
  const rightChecked = intersection(checked, right);

  const handleToggle = (value) => () => {
    const currentIndex = checked.indexOf(value);
    const newChecked = [...checked];

    if (currentIndex === -1) {
      newChecked.push(value);
    } else {
      newChecked.splice(currentIndex, 1);
    }

    setChecked(newChecked);
  };

  const numberOfChecked = (items) => intersection(checked, items).length;

  const handleToggleAll = (items) => () => {
    if (numberOfChecked(items) === items.length) {
      setChecked(not(checked, items));
    } else {
      setChecked(union(checked, items));
    }
  };

  const handleCheckedRight = () => {
    setRight(right.concat(leftChecked));
    setLeft(not(left, leftChecked));
    setChecked(not(checked, leftChecked));
  };

  const handleCheckedLeft = () => {
    setLeft(left.concat(rightChecked));
    setRight(not(right, rightChecked));
    setChecked(not(checked, rightChecked));
  };

  const customList = (title, items) => (
    <Card>
      <CardHeader
        sx={{ px: 2, py: 1 }}
        avatar={
          <Checkbox
            onClick={handleToggleAll(items)}
            checked={numberOfChecked(items) === items.length && items.length !== 0}
            indeterminate={
              numberOfChecked(items) !== items.length && numberOfChecked(items) !== 0
            }
            disabled={items.length === 0}
            inputProps={{
              'aria-label': 'all items selected',
            }}
          />
        }
        title={title}
        subheader={`${numberOfChecked(items)}/${items.length} selected`}
      />
      <Divider />
      <List
        sx={{
          width: 200,
          height: 230,
          bgcolor: 'background.paper',
          overflow: 'auto',
        }}
        dense
        component="div"
        role="list"
      >
        {items.map((value) => {
          const labelId = `transfer-list-all-item-${value}-label`;

          return (
            <ListItem
              key={value}
              role="listitem"
              button
              onClick={handleToggle(value)}
            >
              <ListItemIcon>
                <Checkbox
                  checked={checked.indexOf(value) !== -1}
                  tabIndex={-1}
                  disableRipple
                  inputProps={{
                    'aria-labelledby': 'labelId',
                  }}
                />
              </ListItemIcon>
              <ListItemText id={labelId} primary={value} />
            </ListItem>
          );
        })}
        <ListItem />
      </List>
    </Card>
  );

  return (
    <Stack>
    <h3>Airbnb Finder</h3>
    
    <FormControl sx={{ m: 3 }} component="fieldset" variant="standard">
      <FormLabel component="legend">1. Select Your Room Type</FormLabel>
      <div>
        <FormGroup>
          <FormControlLabel
            control={
              <Checkbox checked={entire} onChange={handleChange} name="entire" />
            }
            label="Entire home/apt"
          />
          <FormControlLabel
            control={
              <Checkbox checked={pv} onChange={handleChange} name="pv" />
            }
            label="Private room"
          />
          <FormControlLabel
            control={
              <Checkbox checked={shared} onChange={handleChange} name="shared" />
            }
            label="Shared room"
          />
        </FormGroup>
      </div>
      <FormLabel component="legend">2. Select Your Price Range</FormLabel>
      <div>
        <Box
        component="form"
        sx={{
          '& > :not(style)': { m: 1, width: '25ch' },
        }}
        noValidate
        autoComplete="off"
      >
        <TextField
          id="min price"
          label="Min Price ($CAD)"
          onChange={handleTextChange}
        />
        <TextField
          id="max price"
          label="Max Price ($CAD)"
        />
      </Box>
    </div>
    <FormLabel component="legend">3. Preference - Choose items in order of your importance </FormLabel>
    <div>
      <Grid container spacing={2} justifyContent="center" alignItems="center">
        <Grid item>{customList('Choices', left)}</Grid>
        <Grid item>
          <Grid container direction="column" alignItems="center">
            <Button
              sx={{ my: 0.5 }}
              variant="outlined"
              size="small"
              onClick={handleCheckedRight}
              disabled={leftChecked.length === 0}
              aria-label="move selected right"
            >
              &gt;
            </Button>
            <Button
              sx={{ my: 0.5 }}
              variant="outlined"
              size="small"
              onClick={handleCheckedLeft}
              disabled={rightChecked.length === 0}
              aria-label="move selected left"
            >
              &lt;
            </Button>
          </Grid>
        </Grid>
        <Grid item>{customList('Chosen', right)}</Grid>
      </Grid>
    </div>
    </FormControl>
    <Button variant="contained" onClick={handleSubmit}>Find!</Button>
    </Stack>
  );
}

export default App;