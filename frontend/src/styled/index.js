// put styled components in here. create new files in this folder if necessary.
// import wherever necessary
import styled from 'styled-components'

export const Button = styled.button`
  background-color: #E47D31;
  cursor: pointer;
  color: white;
  padding: 0.75rem 3rem;
  font-size: 1.25rem;
  border-radius: 30px;
  border: none;
  outline: none;
  transition: background-color 0.2s;
  &:hover {
    background-color: #c96722;
  }
`;

