// put styled components in here. create new files in this folder if necessary.
// import wherever necessary
import styled from 'styled-components'

export const Button = styled.button`
  background-color: #E47D31;
  color: white;
  padding: 0.75rem;
  font-size: 1em;
  border-radius: 30px;
  border: none;
  outline: none;
  transition: background-color 0.2s;
  &:hover {
    background-color: grey;
  }
`;

