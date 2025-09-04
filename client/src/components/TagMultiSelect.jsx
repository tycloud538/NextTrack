import AsyncSelect from "react-select/async";

import { getTags } from "../api";

const selectStyles = {
  control: (provided) => ({
    ...provided,
    width: "300px",
    borderRadius: "0.75rem",
  }),
  multiValueRemove: (provided) => ({
    ...provided,
    ":hover": {
      backgroundColor: "hsl(0 0 80)",
      color: undefined,
    },
  }),
};

export const TagMultiSelect = ({ onChange }) => {
  const getTagOptions = async (search) => {
    const { tags } = await getTags(search);
    return tags.map((tag) => ({
      value: tag.id,
      label: tag.name,
    }));
  };

  const handleChange = (selectedOptions) => {
    onChange(selectedOptions.map((option) => option.value));
  };

  return (
    <AsyncSelect
      styles={selectStyles}
      isMulti
      cacheOptions
      defaultOptions
      loadOptions={getTagOptions}
      onChange={handleChange}
      placeholder="Select genres that you like.."
    />
  );
};
