// __tests__/10-update_uniq_items.test.js
import updateUniqueItems from '../10-update_uniq_items.js';
import groceriesList from '../9-groceries_list.js';

describe('updateUniqueItems', () => {
  it('should update the quantity to 100 for items with initial quantity 1', () => {
    const map = groceriesList();
    updateUniqueItems(map);
    expect(map.get('Pasta')).toBe(100);
    expect(map.get('Rice')).toBe(100);
  });

  it('should not update quantities other than 1', () => {
    const map = groceriesList();
    updateUniqueItems(map);
    expect(map.get('Apples')).toBe(10);
    expect(map.get('Tomatoes')).toBe(10);
    expect(map.get('Banana')).toBe(5);
  });

  it('should throw an error if the argument is not a map', () => {
    expect(() => updateUniqueItems({})).toThrow('Cannot process');
  });
});
