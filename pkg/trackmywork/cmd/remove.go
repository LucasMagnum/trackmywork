package cmd

import (
    "fmt"
    "strings"
    "github.com/spf13/cobra"
)


func NewRemoveCommand() *cobra.Command {

    cmd := &cobra.Command{
      Use:   "remove",
      Short: "Remove task",
      Run: func(cmd *cobra.Command, args []string) {
        fmt.Println("Remove command yey!: " + strings.Join(args, " "))
      },
    }

    return cmd
}
